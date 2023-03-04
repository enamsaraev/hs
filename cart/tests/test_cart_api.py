import pytest
import json

from mixer.backend.django import mixer
from decimal import Decimal
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import ProductInventory

BASE_URL = 'http://127.0.0.1:8000'
GET_ENPOINT = 'cart/'
POST_ENDPOINT = 'cart/add/'
DELETE_ENDPOINT = 'cart/delete/'


pytestmark = [pytest.mark.django_db]


api = APIClient()


@pytest.fixture
def get_hoodie_black_product():
    """Retrieving a product"""

    product = mixer.blend(
        ProductInventory,
        slug='hoodie-black',
        retail_price=Decimal('97.00') 
    )

    return product


@pytest.mark.cartapi
def test_cart_initialize():
    """Test cart initialize successfully"""

    res = api.get(reverse('cart:return_cart'), HTTP_TOKEN='sgdvls')

    assert res.json() is not None


@pytest.mark.cartapi
def test_cart_initialize_without_headers():
    """Test cart initialize successfully"""

    unsucc_res = api.get(reverse('cart:return_cart'))
    assert unsucc_res.status_code == 400


@pytest.mark.cartapi
@pytest.mark.parametrize(
    'quantity, size, color, update',
    [ 
        (2, 'M', 'White', False),
    ]
)
def test_cart_adding_a_product(get_hoodie_black_product, quantity, color, size, update):
    """Test adding a single product to the cart session"""

    response_data = {
        'product_slug': 'hoodie-black',
        'quantity': quantity,
        'size': size,
        'color': color,
        'update': update,
    }

    res = api.post(reverse('cart:add_or_update_cart'), HTTP_TOKEN='sgdvls', data=response_data)
    res_data = res.json()

    assert res.status_code == 201
    assert res_data['items'][f'hoodie-black/{size}/{color}']['quantity'] == quantity
    assert res_data['items'][f'hoodie-black/{size}/{color}']['price'] == '97.00'
    assert res_data['total'] == str(Decimal('97.00') * quantity)


@pytest.mark.cartapi
@pytest.mark.parametrize(
    'quantity, size, color, update',
    [ 
        (2, 'M', 'White', False),
    ]
)
def test_removing_a_product_form_the_cart_session(get_hoodie_black_product, quantity, size, color, update):
    """Test a single product is removed from the cart successfully"""

    response_data = {
        'product_slug': 'hoodie-black',
        'quantity': quantity,
        'size': size,
        'color': color,
        'update': update,
    }

    res = api.post(reverse('cart:add_or_update_cart'), HTTP_TOKEN='sgdvls', data=response_data)
    assert res.status_code == 201

    del_res = api.delete(reverse('cart:delete_cart_product'), HTTP_TOKEN='sgdvls', data={'product_slug': f"{response_data['product_slug']}/{response_data['size']}/{response_data['color']}"})
    assert del_res.status_code == 200


# {"product_slug": "hoodie-black", "quantity": "2", "size": "M", "color": "White", "update": "False"}
# {"name": "name", "email": "email@mail.com", "phone": "12345", "coupon_discount": "0", "total_price": "194.00"}
# 5555555555554477