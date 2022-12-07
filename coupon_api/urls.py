from django.urls import path

from coupon_api.views import check_coupon


app_name = 'coupon'

urlpatterns = [
    path('check/', check_coupon, name='coupon_check'),
]