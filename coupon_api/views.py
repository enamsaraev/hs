from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from coupon_api.models import Coupon


@api_view(['POST'])
def check_coupon(request, *args, **kwargs):
    """Check if coupon is valid"""

    coupon = None
    time_now = timezone.now()

    try:
        coupon = Coupon.objects.get(
            code__iexact=request.data['code'],
            valid_from__lte=time_now,
            valid_to__gte=time_now,
            is_active=True
        )

    except ObjectDoesNotExist:
        return Response({'msg': 'Coupon is expired'}, status=status.HTTP_404_NOT_FOUND)

    if coupon.get_count() == 0:
        return Response({'msg': 'Coupon is unavailable'}, status=status.HTTP_400_BAD_REQUEST)

    coupon.set_minus_count()

    return Response({'msg': 'ok'}, status=status.HTTP_200_OK)
