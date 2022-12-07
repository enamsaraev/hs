import pytest

from mixer.backend.django import mixer

from coupon_api.models import Coupon
from core.models import ProductInventory, Size, Color, Variation
from orders.models import Order, OrderItems
from orders.order_components import OrderComponent


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
def set_cart_session_data():
    """Setting a session data"""

    cart = {
        'first_item': {
            'quantity': 2,
            'price': '678.07',
            'size': 'M',
            'color': 'White'
        },
        'second_item': {
            'quantity': 3,
            'price': '7654.14',
            'size': 'S',
            'color': 'Black'
        }
    }

    return cart


def test_class_order_set_order_component():
    """Test a part od an order creation post method"""

    coupon_model = None
    order = OrderComponent({})

    data = {
        'name': 'FAck',
        'email': 'ffffff@mail.com',
        'phone': '88000000000',
        'coupon_discount': 20,
        'total_price': 5678.09
    }

    bool, res = order.set_order(data, coupon_model)
    order = Order.objects.get(name=data['name'])

    assert bool == True
    assert order.name == data['name']
    assert order.coupon == coupon_model


def test_class_order_set_order_data_component(set_cart_session_data, set_var):
    """Test a part of an order creation post method"""
    
    order = OrderComponent(set_cart_session_data)
    current_order_model = mixer.blend(Order)

    var_before = Variation.objects.last()
    assert var_before.count == var_before.count

    order.set_order_data(current_order_model)

    res = OrderItems.objects.all()[0:2]

    var_after = Variation.objects.last()
    assert var_after.count == var_before.count - set_cart_session_data['second_item']['quantity']

    assert res[0].product_variation == Variation.objects.get(size=Size.objects.get(value='M'))
    assert res[1].product_variation == Variation.objects.get(size=Size.objects.get(value='S'))
