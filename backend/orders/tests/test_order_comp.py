import pytest

from mixer.backend.django import mixer
from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.test import APIRequestFactory

from core.models import ProductInventory, Size, Color, Variation
from orders.models import Order, OrderItems
from orders.order_components import OrderComponent, OrderSetCount
from cart.cart import Cart


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def set_var():
    """Create variation models"""

    prod1 = mixer.blend(ProductInventory, slug='first_item', retail_price=678.07)
    size1 = mixer.blend(Size, value='M')
    color1 = mixer.blend(Color, value='White')
    mixer.blend(Variation, product=prod1, size=size1, color=color1, count=10)

    prod2 = mixer.blend(ProductInventory, slug='second_item', retail_price=7654.14)
    size2 = mixer.blend(Size, value='S')
    color2 = mixer.blend(Color, value='Black')
    mixer.blend(Variation, product=prod2, size=size2, color=color2, count=5)


@pytest.fixture
def set_cart_session_data(db):
    """Retrieving a cart with some session data"""

    fct = APIRequestFactory()

    token_headers = {'HTTP_TOKEN': 'token'}
    request = fct.get(
        'http://127.0.0.1:8000/cart/', 
        **token_headers,
    )

    middleware = SessionMiddleware(lambda x: None)
    middleware.process_request(request)

    request.session['token'] = {
        'items': {
            "first_item/M/White": {
                "size": "M",
                "color": "White",
                "quantity": 2,
                "price": "678.07",
                "total_item_price": "1356.14"
            },
            "second_item/S/Black": {
                "size": "S",
                "color": "Black",
                "quantity": 5,
                "price": "7654.14",
                "total_item_price": "38270.70"
            }
        },
        'total': '39626.84',
        'discount': {
            "code": "",
            "percent": 0,
            "purchased": False
        }
    }
    request.session.save()

    return request


def test_class_order_set_order_component(set_cart_session_data):
    """Test a part od an order creation post method"""

    cart = Cart(set_cart_session_data)

    coupon_model = None
    order_comp = OrderComponent(cart)

    data = {
        'name': 'FAck',
        'email': 'ffffff@mail.com',
        'phone': '88000000000',
        'coupon_discount': 20,
        'total_price': 5678.09
    }

    order_comp.set_order(data, coupon_model)
    order = Order.objects.get(name=data['name'])

    assert order.name == data['name']
    assert order.coupon == coupon_model


def test_dataclass_order_set_count_data(set_cart_session_data, set_var):
    """Test a part of an order creation post method"""
    
    cart = Cart(set_cart_session_data)

    order = OrderComponent(cart)
    current_order_model = mixer.blend(Order)

    var_before = Variation.objects.last()
    assert var_before.count == var_before.count

    OrderSetCount(cart.get_cart(), current_order_model.id)

    res = OrderItems.objects.all()[0:2]

    var_after = Variation.objects.last()
    assert var_after.count == var_before.count - cart.get_cart()['items']['second_item/S/Black']['quantity']

    assert res[0].product_variation == Variation.objects.get(size=Size.objects.get(value='M'))
    assert res[1].product_variation == Variation.objects.get(size=Size.objects.get(value='S'))
