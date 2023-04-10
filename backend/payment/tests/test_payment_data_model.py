import pytest

from mixer.backend.django import mixer

from payment.models import PaymentData
from orders.models import Order


def test_create_payment_data_model(db, payment_data_factory):
    """Test successful payment data model creation"""

    order = mixer.blend(Order)
    payment = payment_data_factory.create(order=order)

    assert payment.order == order