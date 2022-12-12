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


def test_init(init):
    send_mail(**ARGS)

    init.assert_called_once_with(**ARGS)


def test_call(call):
    send_mail(**ARGS)

    call.assert_called_once()