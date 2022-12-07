from django.shortcuts import get_object_or_404

from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from cart.cart import Cart
from cart.serializers import CartDataSerializer

from core.models import ProductInventory

class CartApiView(APIView):
    """Cart views"""

    @staticmethod
    def get_session_cart(request):

        if 'HTTP_TOKEN' not in request.META:
            raise ParseError()

        token = request.META.get('HTTP_TOKEN')
        session = request.session

        cart = Cart(session, token)

        return cart

    def get(self, request, *args, **kwargs):
        """Cart retrieving"""

        cart = self.get_session_cart(request)

        return Response({'cart': cart.get_cart(), 'total_price': cart.get_total_price()}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Cart add or update"""

        cart = self.get_session_cart(request)
        ser = CartDataSerializer(data=request.data)

        if ser.is_valid():  
            product = get_object_or_404(ProductInventory, slug=request.data['product_slug'])

            cart.add_or_update(
                product,
                quantity=ser.data['quantity'],
                size=ser.data['size'],
                color=ser.data['color'],
                update=ser.data['update']
            )

            return Response({'cart': cart.get_cart(), 'total_price': cart.get_total_price()}, status=status.HTTP_201_CREATED)

        return Response({'msg': 'Bad input data'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """Cart delete product"""

        cart = self.get_session_cart(request)

        product = get_object_or_404(ProductInventory, slug=request.data['product_slug'])
        cart.delete(product)

        return Response({'cart': cart.get_cart(), 'total_price': cart.get_total_price()}, status=status.HTTP_200_OK)
