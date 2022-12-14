from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.cart import Cart

from coupon_api.coupon import CouponHelper
from coupon_api.models import Coupon


@api_view(['POST'])
def check_coupon(request, *args, **kwargs) -> Response:
    """Check if coupon is valid"""

    coupon = CouponHelper()
    coupon_check = coupon.set_coupon(code=request.data['code'])
    print(coupon_check)
    if isinstance(coupon_check, int):
        cart = Cart(request)
        cart.set_discount(coupon.coupon.discount)

        return Response({'msg': 'ok'}, status=status.HTTP_200_OK)

    return Response({'msg': 'None'}, status=status.HTTP_200_OK)


#{"code": "GTrDe56OPL"}