from __future__ import absolute_import, unicode_literals

import json
import time

from yookassa import Payment
from celery import shared_task

from orders.models import Order
from orders.order_components import OrderComponent, OrderSetCount

from payment.models import PaymentData


@shared_task
def check_payments_status(payment_id: str, order_id: int, cart: dict, *args, **kwargs):
    """Checking a paymnet status"""

    starttime = time.time()

    order = Order.objects.get(id=order_id)
    pd = PaymentData.objects.create(
        payment_id=payment_id,
        order=order
    )

    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        time.sleep(10.0 - ((time.time() - starttime) % 10.0))

    if payment['status'] == 'succeeded':
        order.set_is_paid()
        pd.set_is_paid()

        OrderSetCount(
            cart=cart,
            order_id=order_id
        )()
        