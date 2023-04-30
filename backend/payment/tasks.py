from __future__ import absolute_import, unicode_literals

import json
import asyncio

from yookassa import Payment
from celery import shared_task

from orders.models import Order
from orders.order_components import OrderComponent, OrderSetCount

from payment.models import PaymentData


async def check_payments_status(payment_id: str, order_id: int, cart: dict):
    """Checking a paymnet status"""

    payment = json.loads((Payment.find_one(payment_id)).json())
    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        await asyncio.sleep(3)

    if payment['status']=='succeeded':
        order = Order.objects.get(id=order_id)
        order.set_is_paid()

        OrderSetCount(
            cart=cart,
            order_id=order_id
        )()

        PaymentData.objects.create(
            payment_id=payment_id,
            order=order
        )
        