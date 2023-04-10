import pytest

from mixer.backend.django import mixer

from django.urls import reverse


CATALOG_URL = reverse('ecommerce:catalog')


@pytest.mark.ecommerce
@pytest.mark.django_db
def test_retrieving_a_catalog_list(client, product_factory):
    """Test retrieving a list of categories"""

    product_factory.create_batch(3)
    response = client.get(CATALOG_URL)

    assert len(response.data) == 3


@pytest.mark.ecommerce
def test_retrieving_a_products_by_category_list(db, client, product_factory, product_inventory_factory):
    """Test retrieving a list of categories"""

    mixer.cycle(5).blend('core.productinventory', slug='fckn')
    response = client.get(reverse('ecommerce:clothes-list'))

    assert len(response.data) == 5


@pytest.mark.ecommerce
def test_product_cart_retrieving_images(db, client, product_factory, product_inventory_factory):
    """Test on retrieving an img"""

    product_inventory_factory.create(product=product_factory.create(slug='fckn'), slug='aboba')
    response = client.get(reverse('ecommerce:clothes-detail'), kwargs={'pk': 1})

    assert response.status_code == 200
    assert 'medias' in response.data['product']

