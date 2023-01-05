from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from orders.models import Order

from cart.cart import Cart

from mailing.tasks import send_mail
from mailing.helpers import MsgHelper


@api_view(['POST'])
def send_notification_mail_with_payed_order(request, *args, **kwargs) -> Response:
    """Retrun payment success info
       Check if payment is successful"""
       
    order = get_object_or_404(Order, id=int(request.data['id']))
    cart = Cart(request)
    msg = MsgHelper(cart.get_cart())()

    send_mail.delay(
        to='test@mail.com',
        message=msg,
        subject=f'BABYEVE Заказ №{order.id}',
        order_id=order.id
    )
    return Response(status=status.HTTP_200_OK)

# {"id": "12", "price": "194.00", "description": "text"}