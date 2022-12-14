import pytest

from rest_framework.test import APIClient

from payment.yk import create_payment


api = APIClient()


@pytest.fixture
def return_purchase_data():
    """Retrieving a payment data"""

    return create_payment(
        '1234.07', 'some products to the pay method'
    )

def test_purchasing_a_confirmation_yookassa_url():
    """Test getting a conf url"""

    data = create_payment(
        '1234.07', 'some products to the pay method'
    )

    assert data['id'] in data['confirmation']['confirmation_url']

# def test_success_payment_status(return_purchase_data):
#     """Test on success payment status"""

#     data = return_purchase_data
#     res = check_payment(data['id'])
    
#     assert res['status']