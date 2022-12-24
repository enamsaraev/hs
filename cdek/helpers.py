import requests, json


def get_calculate_total_amount(to_location: str, token: str):

    response_data = {
        "type": 1,
        "date": "2020-11-03T11:49:32+0700",
        "currency": 1,
        "lang": "rus",
        "from_location": {
            "code": 137,
        },
        "to_location": {
            "code": to_location,
        },
        "packages": [
            {
                "height": 10,
                "length": 10,
                "weight": 4000,
                "width": 10
            }
        ]
    }

    amount = requests.post('https://api.edu.cdek.ru/v2/calculator/tarifflist', headers={'Authorization': f'Bearer {token}'}, json=response_data)
    
    return amount.json()

def auth_cdek_and_get_amount(to_location: str):

    auth = requests.post(
        'https://api.edu.cdek.ru/v2/oauth/token?parameters', 
        data={
            'grant_type': 'client_credentials',
            'client_id': 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI',
            'client_secret': 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
        }
    )
    token = auth.json().get('access_token')

    return get_calculate_total_amount(to_location, token)

