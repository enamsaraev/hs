from payment.yk import create_payment
from payment.tasks import check_payments_status
from mailing.tasks import send_mail


def get_create_payment(
        price: str, description: str, order_id: int, 
        to: str, message: str
    ) -> dict:
    """Get a redirect url"""

    payment_data = create_payment(
        price=price,
        description=description,
    )

    check_payments_status.delay(
        payment_id=payment_data['id'],
        order_id=order_id
    )

    send_mail.delay(
        payment_id=payment_data['id'],
        to=to,
        message=message,
        subject=f'BABYEVE Заказ №{order_id}',
        order_id=order_id
    )

    return payment_data