import pytest

from mixer.backend.django import mixer

from core.models import ProductInventory
from mailing.helpers import MsgHelper


@pytest.fixture
def cart_data():
    """Return cart session data"""

    return {
            "items": {
                "hoodie-black": {
                    "size": "M",
                    "color": "White",
                    "quantity": 2,
                    "price": "97.00",
                    "total_item_price": "194.00"
                }
            },
            "total": "194.00",
            "discount": {
                "code": "",
                "percent": 0,
                "purchased": False
            }
        }

def test_msg_helper_call(db, cart_data):
    """"""
    mixer.blend(ProductInventory, slug='hoodie-black', name='Huinya')

    msg = MsgHelper(cart_data)()

    assert msg == 'Huinya: размер M, цвет White'
