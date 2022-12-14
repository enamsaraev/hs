from rest_framework import serializers


class OrderIdSerializer(serializers.Serializer):
    """Serialize payment id"""

    id = serializers.IntegerField()