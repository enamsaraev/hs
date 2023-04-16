import requests, json
from typing import List

from rest_framework.exceptions import ParseError


class CDEKHelper:
    def __init__(self) -> None:
        auth = requests.post(
            'https://api.edu.cdek.ru/v2/oauth/token?parameters/', 
            data={
                "grant_type": "client_credentials",
                "client_id": "EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI",
                "client_secret": "PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG"
            },
        )
        if auth.status_code == 200:
            self.token = auth.json().get('access_token')
        else:
            return auth.status_code
        
    def get_offices(self, city: str) -> List:
        city_code = self._get_city_code(city=city)

        if city_code:
            offices = self._get_list_of_offices_in_current_city(city_code=int(city_code))
            amount = self._get_calculate_total_amount(city_code=city_code)

            if amount and offices:
                addresses = self._parse_offices(offices=offices)
                return {
                    'addresses': addresses,
                    'amount': amount
                }
        
        return None

    def _get_city_code(self, city) -> str:
        resp = requests.get(
            f'https://api.edu.cdek.ru/v2/location/cities/?city={city}&size=1&page=0', 
            headers={'Authorization': f'Bearer {self.token}'}
        )
        if len(resp.json()) > 0:
            code = resp.json()[0].get('code')
            return code
            
        return None
    
    def _get_list_of_offices_in_current_city(self, city_code: int) -> List:

        offices = requests.get(
            f'https://api.edu.cdek.ru/v2/deliverypoints?city_code={city_code}', 
            headers={'Authorization': f'Bearer {self.token}'}, 
            )

        return offices.json()
    
    def _parse_offices(self, offices: List[dict]):
        list_of_offices_addresses = []

        for office_info in range(len(offices)):
            list_of_offices_addresses.append(offices[office_info]['location'].get('address'))

        return list_of_offices_addresses
    
    def _get_calculate_total_amount(self, city_code: str) -> List[dict]:

        response_data = {
            "type": 1,
            "date": "2020-11-03T11:49:32+0700",
            "currency": 1,
            "tariff_code": 136,
            "lang": "rus",
            "from_location": {
                "code": 137,
            },
            "to_location": {
                "code": city_code,
            },
            "services": [
                {
                    "code": "CARTON_BOX_M",
                    "parameter": "2"
                }
            ],
            "packages": [
                {
                    "height": 15,
                    "length": 33,
                    "weight": 3000,
                    "width": 25
                }
            ]
        }

        amount = requests.post(
            'https://api.edu.cdek.ru/v2/calculator/tariff', 
            headers={'Authorization': f'Bearer {self.token}'}, 
            json=response_data
        )
        return amount.json()