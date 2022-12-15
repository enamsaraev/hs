from rest_framework import serializers

from core import models


class CategorySerializer(serializers.ModelSerializer):
    """Catalog serializer"""

    class Meta:
        model = models.Category
        fields = ('name', 'slug',)


class ProductSerializer(serializers.ModelSerializer):
    """Product serializer"""

    class Meta:
        model = models.Product
        fields = ('name', 'slug')


class SizeSerializer(serializers.ModelSerializer):
    """Size serializer"""

    class Meta:
        model = models.Size
        fields = ('value',)


class ColorSerializer(serializers.ModelSerializer):
    """Size serializer"""

    class Meta:
        model = models.Color
        fields = ('value',)


class VariationSerializer(serializers.ModelSerializer):
    """Variation serializer"""

    color = ColorSerializer()
    size = SizeSerializer()

    class Meta:
        model = models.Variation
        fields = ('color', 'size')


class ProductInventoryCardSerializer(serializers.ModelSerializer):
    """Product inventory card serializer"""

    variations = VariationSerializer(many=True)

    class Meta:
        model = models.ProductInventory
        fields = ('name', 'retail_price', 'description', 'variations',)


class ProductInventorySerializer(serializers.ModelSerializer):
    """Product inventory list serializer"""

    class Meta:
        model = models.ProductInventory
        fields = ('name', 'retail_price', 'description',)