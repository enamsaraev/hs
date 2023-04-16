from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count

from core import models
from ecommerce_api import serializers


class CatalogList(ListAPIView):
    """Retrieving a list of categories"""

    serializer_class = serializers.CatalogSerializer
    queryset = models.Product.objects.filter(is_deleted=False)


class ProductInventoryViewSet(ModelViewSet):
    """MVS for the prod inv model"""

    queryset = models.Product.objects.prefetch_related('product_inventory','product_inventory__medias')
    serializer_class = serializers.ProductSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter,)
    permission_classes = (AllowAny,)
    filterset_fields = ('slug',)
    search_fields = ('product_inventory__slug',)
    ordering_fields = ('product_inventory__retail_price', 'product_inventory__name',)
    http_method_names = ('get',)


    def retrieve(self, request, *args, **kwargs):

        queryset = models.Variation.objects.select_related('product').prefetch_related(
            'color', 'size',
        ).annotate(len_size=Count('size'), len_color=Count('color')).filter(
            product__id=kwargs['pk'], is_deleted=False, count__gt=0, len_size=1, len_color=1,
        )
        serializer = serializers.VariationDetailSerializer(queryset, many=True)

        return Response(serializer.data)