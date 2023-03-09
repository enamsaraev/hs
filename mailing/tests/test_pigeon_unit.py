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

    return mixer.blend(EmailEntry, order=return_order_for_mail)

@pytest.mark.parametrize(('to, text, subject'), [ 
    ('fcknu@mail.com', 'text', 'subject')
])
def test_msg_params(return_order_for_mail, to, text, subject):
    """Test Pigeon init"""

    order = mixer.blend(Order)
    pigeon = Pigeon(to=to, text=text, subject=subject, order_id=return_order_for_mail.id)

    assert pigeon.to == to
    assert pigeon.text == text
    assert pigeon.subject == subject
    assert pigeon.order_id == return_order_for_mail.id



