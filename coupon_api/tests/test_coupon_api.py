import pytest
import requests

from django.urls import reverse
from freezegun import freeze_time
from mixer.backend.django import mixer
from coupon_api.models import Coupon
from rest_framework.test import APIClient

BASE_URL = 'http://127.0.0.1:8000'
CHECK_ENPOINT = 'coupon/check/'


pytestmark = [pytest.mark.django_db]


api = APIClient()


@pytest.fixture
def set_coupons():
    """Create a coupon model"""

    mixer.blend(Coupon, code='GTrDe56OPL', valid_from='2022-11-20 22:14:18', valid_to='2022-12-20 22:14:18', count=20)
    mixer.blend(Coupon, code='HU87TgbRR', valid_from='2022-11-20 22:14:18', valid_to='2022-12-20 22:14:18', count=0)


@freeze_time('2021-11-24')
@pytest.mark.parametrize(
    'code, valid_from, valid_to, count, discount',
    [ 
        (
            'Df34RTuIp', 
            '2021-11-24 22:14:18', 
            '2021-12-24 22:14:18',
            10,
            30,
        ),
    ]
)
def test_coupon_model_creation_successful(db, coupon_factory, code, valid_from, valid_to, count, discount):
    """Test successful coupon model creation"""

    coupon = coupon_factory.create(
        code=code,
        valid_from=valid_from,
        valid_to=valid_to,
        count=count,
        discount=discount
    )

    assert coupon.code == code
    assert coupon.valid_from == valid_from
    assert coupon.valid_to == valid_to
    assert coupon.count == count
    assert coupon.discount == discount


@pytest.mark.parametrize(
    'code, count, status_code, msg',
    [ 
        ('GTrDe56OPL', 20, 200, 'ok'),
        ('HU87TgbRR', 0, 400, 'None'),
    ]
)
def test_check_coupon(set_coupons, code, count, status_code, msg):
    """Test check coupon"""

    response_data = {
        'code': code
    }

    res = api.post(reverse('coupon:coupon_check'), HTTP_TOKEN='token', data=response_data)

    assert res.status_code == status_code
    assert res.json()['msg'] == msg

    """IF DONT WORK TRY TO UPDATE COUPON.COUNT FIELD"""

def test_coupon_set_minus_count():
    """Test set minus count coupon method"""

    coupon = mixer.blend(Coupon, code='abc', count=5)

    coupon.set_minus_count()

    coupon_after = Coupon.objects.get(code='abc')
    assert coupon_after.get_count() == 4