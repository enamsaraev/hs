import asyncio
import json
from payment.yk import create_payment
from mailing.tasks import send_mail
from orders.models import Order
from orders.order_components import OrderComponent, OrderSetCount

from payment.models import PaymentData
from yookassa import Payment


async def check_payments_status(payment_id: str, order_id: int, cart: dict):
    payment = json.loads((Payment.find_one(payment_id)).json())

    while payment['status'] == 'pending':
        payment = json.loads((Payment.find_one(payment_id)).json())
        await asyncio.sleep(3)

    if payment['status'] == 'succeeded':
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
        
async def get_create_payment(
        price: str, description: str, order_id: int, cart: dict
    ) -> dict:
    
    """Get a redirect url"""
    payment_data = create_payment(
        price=price,
        description=description,
    )

    check_payments_status(
        payment_id=payment_data['id'],
        order_id=order_id,
        cart=cart
    )

    return payment_data


def send_a_mail_wia_created_payment(
        payment_id: str, to: str, message: str, order_id: int,
    ) -> None:

    send_mail.delay(
        payment_id=payment_id,
        to=[to],
        message=message,
        subject=f'BABYEVE Заказ №{order_id}',
        order_id=order_id
    )