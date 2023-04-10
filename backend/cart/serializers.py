from rest_framework import serializers


class CartDataSerializer(serializers.Serializer):
    """Serialize a request data to the cart"""

    product_slug = serializers.CharField(max_length=255)
    quantity = serializers.IntegerField()
    size = serializers.CharField(max_length=20)
    color = serializers.CharField(max_length=20)
    update = serializers.BooleanField()
