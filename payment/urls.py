from django.urls import path

from payment.views import get_create_payment, get_success_payment

urlpatterns = [
    path('create/', get_create_payment),
    path('success/', get_success_payment),
]
