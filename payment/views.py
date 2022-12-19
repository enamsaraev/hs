from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from orders.models import Order

from cart.cart import Cart

from payment.yk import create_payment
from payment.tasks import check_payments_status

from mailing.tasks import send_mail
from mailing.helpers import MsgHelper


@api_view(['POST'])
def send_notification_mail_with_payed_order(request, *args, **kwargs) -> Response:
    """Retrun payment success info
       Check if payment is successful"""
    
    order = Order.objects.get(id=int(request.data['id']))
    cart = Cart(request)
    msg = MsgHelper(cart.get_cart())()
    
    send_mail.delay(
        to='test@mail.com',
        message=msg,
        subject=f'BABYEVE Заказ №{order.id}',
        order_id=order.id
    )
    return Response(status=status.HTTP_200_OK)
    

def get_create_payment(price, description, order_id) -> Response:
    """Get a redirect url"""

    payment_data = create_payment(
        price=price,
        description=description,
    )

    check_payments_status.delay(
        payment_id=payment_data['id'],
        order_id=int(order_id)
    )

    return payment_data

# {"id": "12", "price": "194.00", "description": "text"}