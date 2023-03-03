from django.urls import path
from rest_framework.routers import SimpleRouter

from ecommerce_api import views


app_name = 'ecommerce'


router = SimpleRouter()
router.register('clothes', views.ProductInventoryViewSet, basename='clothes')


urlpatterns = [
    path('catalog/', views.CatalogList.as_view(), name='catalog'),
]
urlpatterns += router.urls