from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Does all migrations and migrate + load all db fixtures"""
    def handle(self, *args: any, **options: any) -> None:
        call_command('makemigrations')
        call_command('migrate')
        call_command('loaddata', 'core_db_category_fixtures')
        call_command('loaddata', 'core_db_product_fixtures')
        call_command('loaddata', 'core_db_product_inventory_fixtures')
        call_command('loaddata', 'core_db_variation_fixtures')
        call_command('loaddata', 'coupon_api_db_coupon_fixtures')