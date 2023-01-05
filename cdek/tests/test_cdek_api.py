# import requests, pytest

# from django.urls import reverse
# from rest_framework.test import APIClient

# from cdek.helpers import get_calculate_total_amount


# api = APIClient()


# @pytest.fixture
# def get_cdek_auth():
#     """Get an auth cdek token to access all api urls"""

#     auth = requests.post(
#         'https://api.edu.cdek.ru/v2/oauth/token?parameters', 
#         data={
#             'grant_type': 'client_credentials',
#             'client_id': 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI',
#             'client_secret': 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
#         }
#     )
#     token = auth.json().get('access_token')

#     return token


# def test_get_totat_amount(get_cdek_auth):
#     """
#         test delivery prices
#         44 - moscow city code
#     """

#     res = get_calculate_total_amount(
#         token=get_cdek_auth,
#         to_location='44',
#     )

#     assert 'tariff_codes' in res


# def test_cdek_get_total_delivery_prices_api():
#     """
#         test cdek calculate all delivery prices
#         44 - moscow city code
#     """

#     data = {
#         'to_location': '44'
#     }
#     response = api.post(reverse('cdek:cdek-calculate-prices'), data=data)
    
#     assert 'tariff_codes' in response.json()['result']