import pytest

from django.core.management import call_command

@pytest.fixture(scope='session')
def db_fixture_setup(django_db_setup, django_db_blocker):
    """
    Load DD data fixtures
    """

    with django_db_blocker.unblock():
        call_command('loaddata', 'core_db_category_fixtures.json')
        call_command('loaddata', 'core_db_product_fixtures.json')
        call_command('loaddata', 'core_db_product_inventory_fixtures.json')
        call_command('loaddata', 'core_db_variation_fixtures.json')
        call_command('loaddata', 'coupon_api_db_coupon_fixtures.json')