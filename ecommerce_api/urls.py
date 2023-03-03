from django.urls import path
from rest_framework.routers import SimpleRouter

from ecommerce_api import views


app_name = 'ecommerce'


router = SimpleRouter()
router.register('clothes', views.ProductInventoryViewSet)


urlpatterns = [
    # path('catalog/', views.CatalogList.as_view(), name='catalog'),
    # path('<slug:slug>/', views.ProductList.as_view(), name='products'),
    # path('<slug:slug>/<slug:product_slug>/', views.ProductInventoryView.as_view(), name='product_card'),
]
urlpatterns += router.urls