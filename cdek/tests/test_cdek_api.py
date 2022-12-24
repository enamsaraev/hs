import requests, pytest

from cdek.helpers import get_calculate_total_amount


@pytest.fixture
def get_cdek_auth():
    """Get an auth cdek token to access all api urls"""

    auth = requests.post(
        'https://api.edu.cdek.ru/v2/oauth/token?parameters', 
        data={
            'grant_type': 'client_credentials',
            'client_id': 'EMscd6r9JnFiQ3bLoyjJY6eM78JrJceI',
            'client_secret': 'PjLZkKBHEiLK3YsjtNrt3TGNG0ahs3kG'
        }
    )
    token = auth.json().get('access_token')

    return token


def test_get_totat_amount(get_cdek_auth):
    """
        test delivery prices
        44 - moscow city code
    """

    res = get_calculate_total_amount(
        token=get_cdek_auth,
        to_location='44',
    )

    assert 'tariff_codes' in res