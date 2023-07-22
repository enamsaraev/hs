import requests
import os
from typing import List


class CDEKHelper:
    def __init__(self) -> None or int:
        auth = requests.post(
            'https://api.cdek.ru/v2/oauth/token?parameters', 
            data={
                "grant_type": "client_credentials",
                "client_id": os.environ.get("CDEK_ACC"),
                "client_secret": os.environ.get("CDEK_PASS")
            },
        )
        if auth.status_code == 200:
            self.token = auth.json().get('access_token')
            print(self.token)
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
            f'https://api.cdek.ru/v2/location/cities/?city={city}&size=1&page=0', 
            headers={'Authorization': f'Bearer {self.token}'}
        )
        if len(resp.json()) > 0:
            code = resp.json()[0].get('code')
            return code
            
        return None
    
    def _get_list_of_offices_in_current_city(self, city_code: int) -> List:

        offices = requests.get(
            f'https://api.cdek.ru/v2/deliverypoints?city_code={city_code}', 
            headers={'Authorization': f'Bearer {self.token}'}, 
            )

        return offices.json()
    
    def _parse_offices(self, offices: List[dict]):
        list_of_offices_addresses = []

        for office_info in range(len(offices)):
            list_of_offices_addresses.append(offices[office_info]['location'].get('address'))

        return list_of_offices_addresses
    
    def _get_calculate_total_amount(self, city_code: str) -> List[dict]:

        request_data = {
            "type": 1,
            "currency": 1,
            "tariff_code": 368,
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
                    "parameter": "1"
                }
            ],
            "packages": [
                {
                    "height": 15,
                    "length": 33,
                    "weight": 5000,
                    "width": 25
                }
            ]
        }
        
        amount = requests.post(
            'https://api.cdek.ru/v2/calculator/tariff', 
            headers={'Authorization': f'Bearer {self.token}'}, 
            json=request_data
        )
        return amount.json()