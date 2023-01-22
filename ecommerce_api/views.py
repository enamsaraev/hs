from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from core import models
from ecommerce_api import serializers


class CatalogList(ListAPIView):
    """Retrieving a list of categories"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.filter(is_active=True)


class ProductList(ListAPIView):
    """Retrieving a list of products by category"""

    serializer_class = serializers.ProductInventorySerializer

    def get_queryset(self):
        query =  models.ProductInventory.objects.select_related('product').filter(
            product__slug=self.kwargs['slug'],
            is_active=True
        )
        return query


# class ProductInventoryView(ListAPIView):
#     """Retrieving a product card"""
    
#     serializer_class = serializers.ProductInventoryCardSerializer

#     def get_queryset(self):

#         query = models.Variation.objects.filter(
#             product__product__slug=self.kwargs['slug'],
#             product__slug=self.kwargs['product_slug'],
#             is_active=True
#         ).select_related('product').prefetch_related('size', 'color')

#         query = models.ProductInventory.objects.filter(
#             product__slug=self.kwargs['slug'],
#             slug=self.kwargs['product_slug'],
#             is_active=True
#         ).prefetch_related('variations', 'variations__size', 'variations__color', 'medias')

#         return query


class ProductInventoryView(APIView):

    def get(request, *args, **kwargs):

        prod = models.ProductInventory.objects.filter(
            product__slug=kwargs['slug'],
            slug=kwargs['product_slug'],
            is_active=True
        ).prefetch_related('medias')

        variat = models.Variation.objects.filter(
            product__product__slug=kwargs['slug'],
            product__slug=kwargs['product_slug'],
            is_active=True
        ).prefetch_related('size', 'color')

        return Response(
            {
                'product': serializers.ProductInventorySerializerTest(prod, many=True, read_only=True).data[0],
                'var': serializers.VariationSerializerTest(variat, many=True, read_only=True).data
            }
        )



