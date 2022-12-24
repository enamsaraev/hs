from rest_framework.generics import ListAPIView
from rest_framework.exceptions import NotFound

from core import models
from ecommerce_api import serializers


class CatalogList(ListAPIView):
    """Retrieving a list of categories"""

    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.filter(is_active=True)


class ProductList(ListAPIView):
    """Retrieving a list of products by category"""

    serializer_class = serializers.ProductInventorySerializer
    queryset = models.ProductInventory.objects.all()

    def get_queryset(self):
        query =  self.queryset.filter(
            product__slug=self.kwargs['slug'],
            is_active=True
        )

        if query:
            return query
        
        else:
            raise NotFound()


class ProductInventoryView(ListAPIView):
    """Retrieving a product card"""
    
    serializer_class = serializers.ProductInventoryCardSerializer
    
    def get_queryset(self):
        query =  models.ProductInventory.objects.filter(
            product__slug=self.kwargs['slug']
        ).filter(
            slug=self.kwargs['product_slug'],
            is_active=True
        )

        if query:
            return query
        
        else:
            raise NotFound()