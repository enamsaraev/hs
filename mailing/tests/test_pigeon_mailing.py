import pytest

from mixer.backend.django import mixer

from orders.models import Order
from mailing.tasks import send_mail


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def init(mocker):
    return mocker.patch('mailing.tasks.Pigeon')


@pytest.fixture
def call(mocker):
    return mocker.patch('mailing.tasks.Pigeon.__call__')


ARGS = dict(
    to='test@mail.ru',
    message='msg',
    subject='Ebalo na nol',
    order=None
)

@pytest.fixture
def current_mail_args():
    order = mixer.blend(Order)
    return dict(
        to='test@mail.ru',
        message='msg',
        subject='Ebalo na nol',
        order_id=order.id
    )


def test_init(init, current_mail_args):
    send_mail(**current_mail_args)

    init.assert_called_once_with(**current_mail_args)


def test_call(call, current_mail_args):
    send_mail(**current_mail_args)

    call.assert_called_once()