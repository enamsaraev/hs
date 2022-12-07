from rest_framework import serializers

from coupon_api.models import Coupon


class CouponSerializer(serializers.Serializer):
    """Coupon model serializer"""

    code = serializers.CharField(max_length=50)