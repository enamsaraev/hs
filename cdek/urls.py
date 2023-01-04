from django.urls import path

from cdek.views import get_offices_list


app_name = 'cdek'

urlpatterns = [
    path('prices/', get_offices_list, name='cdek-calculate-prices'),
]