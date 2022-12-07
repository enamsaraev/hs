from django.urls import path

from payment.views import some_func, blabla

urlpatterns = [
    path('as/', some_func),
    # path('bla/', blabla),
]
