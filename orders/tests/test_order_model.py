import pytest
import requests
import json

from mixer.backend.django import mixer

from cart.cart import Cart
from core.models import Variation


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(
    'name, email, phone, coupon_discount, total_price',
    [ 
        ('Dude', 'dude@mail.com', '8-800-000-00-00', 20, 4567.58),
    ]
)
def test_order_model_creation_successful(order_factory, name, email, phone, coupon_discount, total_price):
    """Test successful order model creation"""

    order = order_factory.create(
        name=name,
        email=email,
        phone=phone,
        coupon=mixer.blend('coupon_api.Coupon'),
        coupon_discount=coupon_discount,
        total_price=total_price
    )

    assert order.name == name
    assert order.email == email
    assert order.phone == phone
