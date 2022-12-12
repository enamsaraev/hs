import pytest

from mixer.backend.django import mixer

from django.core.mail import send_mail

from orders.models import Order
from mailing.pigeon import Pigeon


pytestmark = [pytest.mark.django_db]


@pytest.mark.parametrize(('to, message, subject, create_order'), [ 
    ('fcknu@mail.com', 'message', 'subject', False),
    ('fcknu@mail.com', 'message', 'subject', True)
])
def test_msg_params(to, message, subject, create_order):
    """Test Pigeon init"""

    if create_order:
        order = mixer.blend(Order)
    
    else:
        order = None

    pigeon = Pigeon(to=to, message=message, subject=subject, order=order)

    assert pigeon.to == to
    assert pigeon.message == message
    assert pigeon.subject == subject
    assert pigeon.order == order


# def test_return_bad_if_mail_is_already_sent():
#     """Assert fAlse if mail is already sent"""

#     Pigeon(
#         to='fcknu@mail.com', 
#         message='message', 
#         subject='subject', 
#         order=None
#     )()

#     assert len(send_mail.outbox) == 1


