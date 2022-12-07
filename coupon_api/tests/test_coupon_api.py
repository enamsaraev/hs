import pytest
import requests

from django.urls import reverse

from freezegun import freeze_time

from mixer.backend.django import mixer

from coupon_api.models import Coupon

BASE_URL = 'http://127.0.0.1:8000'
CHECK_ENPOINT = 'coupon/check/'


pytestmark = [pytest.mark.django_db]


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
        ('HU87TgbRR', 0, 400, 'Coupon is unavailable'),
    ]
)
def test_check_coupon(client, set_coupons, code, count, status_code, msg):
    """Test check coupon"""

    current_coupon_before = Coupon.objects.get(code=code)
    response_data = {
        'code': code
    }

    assert current_coupon_before.get_count() == count

    res = client.post(reverse('coupon:coupon_check'), data=response_data)
    current_coupon_after = Coupon.objects.get(code=code)

    assert current_coupon_after.get_count() != count or current_coupon_after.get_count() == 0
    assert res.status_code == status_code
    assert res.json()['msg'] == msg