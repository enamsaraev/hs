import string
import random

from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from cart.cart import Cart
from cart.serializers import CartDataSerializer

from core.models import ProductInventory


class CartApiView(APIView):
    """Cart views"""

    @staticmethod
    def get_session_cart(request) -> Cart:
        """Return session cart"""

        cart = Cart(request)
        return cart

    def get(self, request, *args, **kwargs) -> Response:
        """Cart retrieving"""
       
        cart = self.get_session_cart(request)
        return Response(cart.get_cart(), status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs) -> Response:
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

            return Response(cart.get_cart(), status=status.HTTP_201_CREATED)

        return Response({'msg': 'Bad input data'}, status=status.HTTP_400_BAD_REQUEST)


class DeleteCartData(APIView):

    @staticmethod
    def get_session_cart(request) -> Cart:
        """Return session cart"""

        cart = Cart(request)
        return cart
    
    def post(self, request, *args, **kwargs) -> Response:
        """Cart delete product"""

        cart = self.get_session_cart(request)
        cart.delete(request.data['product_slug'])


        return Response(cart.get_cart(), status=status.HTTP_200_OK)
    

class TknGen(APIView):
    def get(self, request, *args, **kwargs):
        tkn_letters_and_digits = string.ascii_letters + string.digits
        tkn = ''.join(random.sample(tkn_letters_and_digits, 30))

        return Response({'token': tkn}, status=status.HTTP_200_OK)
