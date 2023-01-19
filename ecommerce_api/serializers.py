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


class MediaSerializer(serializers.ModelSerializer):
    """Media serializer"""

    class Meta:
        model = models.Media
        fields = ('img',)


class ProductInventorySerializer(serializers.ModelSerializer):
    """Product inventory list serializer"""

    class Meta:
        model = models.ProductInventory
        fields = ('name', 'retail_price', 'description')
    

class ListedSer(serializers.RelatedField):

    def to_representation(self, value):
        return value.value

# class ProductInventoryCardSerializer(serializers.ModelSerializer):

#     color = ListedSer(many=True, read_only=True)
#     size = ListedSer(many=True, read_only=True)
#     name = serializers.CharField(source='product.name')
#     retail_price = serializers.CharField(source='product.retail_price')

#     class Meta:
#         model = models.Variation
#         fields = ('name', 'retail_price', 'color', 'size', 'count',)


class ProductInventorySerializerTest(serializers.ModelSerializer):

    medias = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.ProductInventory
        fields = ('name', 'retail_price', 'medias',)


class VariationSerializerTest(serializers.ModelSerializer):

    color = serializers.StringRelatedField(many=True)
    size = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Variation
        fields = ('color', 'size', 'count',)