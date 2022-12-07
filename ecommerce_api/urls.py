from django.urls import path

from ecommerce_api import views


app_name = 'ecommerce'

urlpatterns = [
    path('catalog/', views.CatalogList.as_view(), name='catalog'),
    path('catalog/<slug:slug>/', views.ProductList.as_view(), name='products'),
    path('catalog/<slug:slug>/<slug:product_slug>/', views.ProductInventoryView.as_view(), name='product_card'),
]