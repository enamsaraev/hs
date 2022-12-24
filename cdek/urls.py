from django.urls import path

from cdek.views import get_offices_list


app_name = 'cdek'

urlpatterns = [
    path('offices/', get_offices_list, name='cdek-city-offices'),
]