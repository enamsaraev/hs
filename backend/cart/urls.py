from django.urls import path

from cart.cart_views import CartApiView


app_name = 'cart'


urlpatterns = [
    path('', CartApiView.as_view(), name='return_cart'),
    path('add/', CartApiView.as_view(), name='add_or_update_cart'),
    path('delete/<slug:slug>/', CartApiView.as_view(), name='delete_cart_product'),
]