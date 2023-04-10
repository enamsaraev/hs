from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.cart import Cart

from coupon_api.coupon import CouponHelper


@api_view(['POST'])
def check_coupon(request, *args, **kwargs) -> Response:
    """Check if coupon is valid"""

    code = request.data['code']

    coupon = CouponHelper()
    discount = coupon.set_coupon(code=code)

    if isinstance(discount, int):
        cart = Cart(request)
        cart.set_discount(code, discount)

        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)

    return Response({'msg': 'None'}, status=status.HTTP_400_BAD_REQUEST)


#{"code": "GTrDe56OPL"}