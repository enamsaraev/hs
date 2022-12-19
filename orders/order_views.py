from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from mailing.helpers import MsgHelper
from cart.cart import Cart
from payment.views import get_create_payment

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
            return Response(
                {
                    'url': payment_data['confirmation']['confirmation_url'],
                },
                status=status.HTTP_200_OK
            )
        
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
