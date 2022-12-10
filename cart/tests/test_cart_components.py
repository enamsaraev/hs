import pytest

from mixer.backend.django import mixer
from django.contrib.sessions.middleware import SessionMiddleware
from rest_framework.test import APIRequestFactory

from cart.cart import Cart
from core.models import ProductInventory


BASE_URL = 'http://127.0.0.1:8000'
GET_ENPOINT = 'cart/'


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def return_request(db):
    """Retrieving a cart with some session data"""

    fct = APIRequestFactory()

    token_headers = {'HTTP_TOKEN': 'token'}
    request = fct.get(
        BASE_URL + '/' + GET_ENPOINT, 
        **token_headers,
    )

    middleware = SessionMiddleware(lambda x: None)
    middleware.process_request(request)

    request.session['token'] = {
        'items': {
            "hoodie-black": {
                "size": "M",
                "color": "White",
                "quantity": 2,
                "price": "97.00",
                "total_item_price": "194.00"
            },
            "item": {
                "size": "S",
                "color": "Pink",
                "quantity": 5,
                "price": "100.00",
                "total_item_price": "500.00"
            }
        },
        'total': 694.00,
        'discount': 0
    }
    request.session.save()

    return request

@pytest.fixture
def return_cart(return_request):
    """Return a cart object"""

    cart = Cart(return_request)
    return cart

def test_cart_init_initialize(return_cart):
    """Test cart init"""

    cart = return_cart
    
    assert 'items' in cart.get_cart()
    assert 'total' in cart.get_cart()
    assert 'discount' in cart.get_cart()


@pytest.mark.parametrize(
    'quantity, size, color, update',
    [ 
        ( 2, 'M', 'White', False)
    ]
)
def test_cart_adding_a_product(return_cart, product, quantity, color, size, update):
    """Test cart add_or_update component"""

    cart = return_cart
    product = mixer.blend(ProductInventory, slug='hod')

    cart.add_or_update(
        product=product,
        quantity=quantity,
        size=size,
        color=color,
        update=update
    )
    assert 'hod' in cart.get_cart()['items']

def test_cart_delete_component(return_cart):
    """Test cart delete method"""

    product = mixer.blend(ProductInventory, slug='item')

    cart = return_cart
    cart.delete(product)

    assert 'item' not in cart.get_cart()['items']

def test_cart_set_discount_component(return_cart):
    """Test set_discoumt cart method"""

    cart = return_cart
    cart.set_discount(20)

    assert cart.get_cart()['discount'] == '20'

def test_cart_get_total_price(return_cart):
    """Test get_total_price cart method"""

    cart = return_cart
    
    assert cart.get_cart()['total'] == '694.00'

def test_cart_clear_all_cart(return_cart):
    """Test clear_all_cart cart method"""

    cart = return_cart
    assert cart.get_cart()['items'] is not None

    cleared_cart = cart.clear_all_cart()
    assert cleared_cart is None



    