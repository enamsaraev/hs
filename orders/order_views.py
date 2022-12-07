from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from orders.order_components import OrderComponent
from orders.serializers import OrderSerializer

from cart.cart import Cart


def get_cart_model(request):
    """Return a cart model for the order"""

    if 'HTTP_TOKEN' not in request.META:
            raise ParseError()

    token = request.META.get('HTTP_TOKEN')
    session = request.session

    cart = Cart(session, token)

    return cart


class OrderApiView(APIView):
    """Class that creates an order model"""

    def post(self, request, *args, **kwargs):
        """Post view"""

        cart = get_cart_model(request)
        order = OrderComponent(cart)

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():
            """Creating an order if serializer data is valid"""

            result_order = order.processing_order(serializer.data)
            if result_order:
                return Response(cart.get_cart(), status=status.HTTP_201_CREATED)
        
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
