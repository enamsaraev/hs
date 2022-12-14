from __future__ import absolute_import, unicode_literals

from ecommerce_celery.celery import app

from orders.models import Order
from mailing.pigeon import Pigeon


@app.task
def send_mail(to: str, message: str, subject: str, order_id: int):
    """Async email sending"""

    Pigeon(
        to=to,
        message=message,
        subject=subject,
        order_id=order_id,
    )()
