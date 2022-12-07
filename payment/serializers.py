from rest_framework import serializers


class PaymentDataSerializer(serializers.Serializer):
    """Serialize payment data"""

    price = serializers.DecimalField(max_digits=9, decimal_places=2)
    description = serializers.CharField(max_length=1000)


class PaymentIdSerializer(serializers.Serializer):
    """Serialize payment id"""

    id = serializers.CharField(max_length=500)