import pytest

from django.urls import reverse


CATALOG_URL = reverse('ecommerce:catalog')


@pytest.mark.ecommerce
@pytest.mark.django_db
def test_retrieving_a_catalog_list(client, category_factory):
    """Test retrieving a list of categories"""

    category_factory.create_batch(3)

    response = client.get(CATALOG_URL)

    assert len(response.data) == 3  # 2 more fixtures are installed in core_db_category_fixtures.json


@pytest.mark.ecommerce
def test_retrieving_a_products_by_category_list(db, client, product_factory, product_inventory_factory):
    """Test retrieving a list of categories"""

    product_inventory_factory.create_batch(5, product=product_factory.create(slug='fckn'))

    response = client.get(reverse('ecommerce:products', kwargs={'slug': 'fckn'}))

    assert len(response.data) == 5

