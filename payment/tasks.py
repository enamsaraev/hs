from __future__ import absolute_import, unicode_literals

import json
import time 

from yookassa import Payment

from celery import shared_task

from orders.models import Order
from payment.models import PaymentData


@shared_task
def check_payments_status(payment_id: str, order_id: int):
    """Checking a paymnet status"""

    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        time.sleep(3)
        print('Checking')

    if payment['status']=='succeeded':
        order = Order.objects.get(id=order_id)
        PaymentData.objects.create(
            payment_id=payment_id,
            order=order
        )
        print('Done')

    elif payment['status'] == 'canceled':
        return False

    return False