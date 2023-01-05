from __future__ import absolute_import, unicode_literals

import json, time

from yookassa import Payment
from celery import shared_task

from ecommerce_celery.celery import app

from mailing.pigeon import Pigeon


def check_succed_payment_retr(payment_id: str):
    """"""

    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        time.sleep(3)

    if payment['status']=='succeeded':
        return True

    return False

@shared_task
def send_mail(payment_id: str, to: str, message: str, subject: str, order_id: int):
    """Async email sending"""

    if check_succed_payment_retr(payment_id):

        Pigeon(
            to=to,
            message=message,
            subject=subject,
            order_id=order_id,
        )()
