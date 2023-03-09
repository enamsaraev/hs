import pytest

from unittest.mock import patch

from mixer.backend.django import mixer

from orders.models import Order
from mailing.tasks import check_succed_payment_retr, send_mail
from mailing.pigeon import Pigeon


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def init(mocker):
    return mocker.patch('mailing.tasks.Pigeon')


@pytest.fixture
def call(mocker):
    return mocker.patch('mailing.tasks.Pigeon.__call__')


@pytest.fixture
def current_order_args():
    return mixer.blend(Order)
    

@patch('mailing.tasks.check_succed_payment_retr')
def test_init(mock_fn, init, current_order_args):
    mock_fn.return_value = True
    send_mail(
        payment_id='hfdhfd67',
        to=['test@mail.ru'],
        message='msg',
        subject='Ebalo na nol',
        order_id=current_order_args.id
    )

    init.assert_called_once_with(
        to=['test@mail.ru'],
        text='msg',
        subject='Ebalo na nol',
        order_id=current_order_args.id
    )