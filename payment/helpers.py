from payment.yk import create_payment
from payment.tasks import check_payments_status
from mailing.tasks import send_mail


def get_create_payment(
        price: str, description: str, order_id: int
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

    return payment_data


def send_a_mail_wia_created_payment(
        payment_id: str, to: str, message: str, order_id: int,
    ) -> None:

    send_mail.delay(
        payment_id=payment_id,
        to=to,
        message=message,
        subject=f'BABYEVE Заказ №{order_id}',
        order_id=order_id
    )