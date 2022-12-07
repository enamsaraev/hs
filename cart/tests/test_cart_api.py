import pytest
import requests

from decimal import Decimal


BASE_URL = 'http://127.0.0.1:8000'
GET_ENPOINT = 'cart/'
POST_ENDPOINT = 'cart/add/'
DELETE_ENDPOINT = 'cart/delete/'


pytestmark = [pytest.mark.django_db]


@pytest.fixture(scope='session')
def get_token_in_headers():
    """Get a header values with token"""

    return {'TOKEN': 'sgdvls'}


@pytest.mark.cartapi
def test_cart_initialize(get_token_in_headers):
    """Test cart initialize successfully"""

    req = requests.Session()
    req.headers.update(get_token_in_headers)

    res = req.get(BASE_URL + '/' + GET_ENPOINT, headers=get_token_in_headers)

    assert res.json() is not None


@pytest.mark.cartapi
@pytest.mark.parametrize(
    'quantity, size, color, update',
    [ 
        (2, 'M', 'White', False),
    ]
)
def test_cart_adding_a_product(client, get_token_in_headers, quantity, color, size, update):
    """Test adding a single product to the cart session"""

    response_data = {
        'product_slug': 'hoodie-black',
        'quantity': quantity,
        'size': size,
        'color': color,
        'update': update,
    }

    res = requests.post(BASE_URL + '/' + POST_ENDPOINT, data=response_data, headers=get_token_in_headers)
    res_data = res.json()

    assert res.status_code == 201
    assert res_data['cart']['hoodie-black']['quantity'] == quantity
    assert res_data['cart']['hoodie-black']['price'] == '97.00'
    assert res_data['total_price']== str(Decimal('97.00') * quantity)


@pytest.mark.cartapi
@pytest.mark.parametrize(
    'quantity, size, color, update',
    [ 
        (2, 'M', 'White', False),
    ]
)
def test_removing_a_product_form_the_cart_session(get_token_in_headers, quantity, size, color, update):
    """Test a single product is removed from the cart successfully"""

    response_data = {
        'product_slug': 'hoodie-black',
        'quantity': quantity,
        'size': size,
        'color': color,
        'update': update,
    }

    res = requests.post(BASE_URL + '/' + POST_ENDPOINT, headers=get_token_in_headers, data=response_data)
    assert res.status_code == 201

    del_res = requests.delete(BASE_URL + '/' + DELETE_ENDPOINT, headers=get_token_in_headers, data={'product_slug': response_data['product_slug']})
    assert del_res.status_code == 200


@pytest.mark.cartapi
def test_cart_initialize_without_headers():
    """Test cart initialize successfully"""

    unsucc_res = requests.get(BASE_URL + '/' + GET_ENPOINT, headers=None)

    assert unsucc_res.status_code == 400


# {"product_slug": "hoodie-black", "quantity": "2", "size": "M", "color": "White", "update": "False"}
# {"name": "name", "email": "email@mail.com", "address": "address", "code": "-", "coupon_discount": "0", "total_price": "194.00"}