from django.urls import path

from payment.views import get_create_payment, send_notification_mail_with_payed_order

urlpatterns = [
    path('send/', send_notification_mail_with_payed_order),
]
