from django.urls import path

from orders.order_views import OrderApiView


app_name = 'orders'


urlpatterns = [
    path('create_order/', OrderApiView.as_view(), name='order_creation'),
]