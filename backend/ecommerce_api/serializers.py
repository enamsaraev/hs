from rest_framework import serializers

from core import models


class CatalogSerializer(serializers.ModelSerializer):
    """Product serializer"""

    class Meta:
        model = models.Product
        fields = ('name', 'slug')


class MediaSerializer(serializers.ModelSerializer):
    """Media serializer"""

    class Meta:
        model = models.Media
        fields = ('img', 'is_default',)


class ProductInventorySerializer(serializers.ModelSerializer):

    # medias = serializers.StringRelatedField(many=True)
    medias = MediaSerializer(many=True)
    parent_slug = serializers.StringRelatedField(source='product.slug')

    class Meta:
        model = models.ProductInventory
        fields = ('id', 'name', 'slug', 'parent_slug', 'retail_price', 'description', 'medias',)

    
class ProductSerializer(serializers.ModelSerializer):
    
    product_inventory = ProductInventorySerializer(many=True)

    class Meta:
        model = models.Product
        fields = ('slug', 'product_inventory')


class VariationDetailSerializer(serializers.ModelSerializer):

    description = serializers.StringRelatedField(source='product.description')
    size = serializers.StringRelatedField(many=True)
    color = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Variation
        fields = ('id', 'color', 'size', 'count', 'description')