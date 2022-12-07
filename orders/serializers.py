from rest_framework import serializers

from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):
    """Serialize order data"""

    code = serializers.CharField(max_length=50)

    class Meta:
        model = Order
        fields = ('name', 'email', 'phone', 'code', 'coupon_discount', 'total_price')