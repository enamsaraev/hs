from django.urls import path

from payment.views import send_notification_mail_with_payed_order

urlpatterns = [
    path('send/', send_notification_mail_with_payed_order, name='send-email'),
]

app_name = 'payment'