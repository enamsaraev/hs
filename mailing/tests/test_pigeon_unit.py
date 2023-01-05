import pytest

from mixer.backend.django import mixer

from django.core.mail import send_mail

from orders.models import Order

from mailing.pigeon import Pigeon
from mailing.models import EmailEntry


pytestmark = [pytest.mark.django_db]


@pytest.fixture
def return_order_for_mail():
    """Return order model"""

    return mixer.blend(Order)

@pytest.fixture
def return_sent_mail(return_order_for_mail):
    """Set an alredy sent mail"""

    return mixer.blend(EmailEntry, order=mixer.blend(Order))

@pytest.mark.parametrize(('to, message, subject'), [ 
    ('fcknu@mail.com', 'message', 'subject')
])
def test_msg_params(return_order_for_mail, to, message, subject):
    """Test Pigeon init"""

    order = mixer.blend(Order)
    pigeon = Pigeon(to=to, message=message, subject=subject, order_id=return_order_for_mail.id)

    assert pigeon.to == to
    assert pigeon.message == message
    assert pigeon.subject == subject
    assert pigeon.order_id == return_order_for_mail.id


def test_return_bad_if_mail_is_already_sent(return_order_for_mail, return_sent_mail):
    """Assert false if mail is already sent"""

    pigeon = Pigeon(
        to=return_sent_mail.email, 
        message=return_sent_mail.message, 
        subject='subject',
        order_id=return_sent_mail.order.id
    )()

    assert pigeon == None



