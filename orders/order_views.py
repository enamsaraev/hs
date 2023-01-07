from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponseRedirect

from mailing.helpers import MsgHelper
from cart.cart import Cart
from payment.helpers import get_create_payment, send_a_mail_wia_created_payment

from orders.order_components import OrderComponent



class OrderApiView(APIView):
    """Class that creates an order model"""

    def post(self, request, *args, **kwargs) -> Response:
        """Post view"""

        cart = Cart(request)
        msg = MsgHelper(cart.get_cart())()
        order = OrderComponent(cart)

        """Creating an order if serializer data is valid"""
        order = order.processing_order(request.data) # создать неоплаченный заказ

        if order:
            payment_data = get_create_payment(
                price=request.data['total_price'],
                description=msg,
                order_id=order.id
            )
            send_a_mail_wia_created_payment(
                payment_id=payment_data['id'],
                to=order.email,
                message=msg,
                order_id=order.id,
            )
            return Response(
                {
                    'url': payment_data['confirmation']['confirmation_url'],
                },

            )
        
        return Response(status=status.HTTP_400_BAD_REQUEST)
