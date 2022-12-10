from rest_framework import serializers


class PaymentIdSerializer(serializers.Serializer):
    """Serialize payment id"""

    id = serializers.CharField(max_length=500)