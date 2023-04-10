import pytest

import requests


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    'name, slug',
    [ 
        ('test_name_f', 'test_slug_f'),
        ('test_name_s', 'test_slug_s'),
    ],
)
def test_category_insert_data(db, category_factory, name, slug):
    """Test category model creation with insert data"""

    category = category_factory.create(name=name, slug=slug)

    assert category.name == name
    assert category.slug == slug


@pytest.mark.dbfixture
@pytest.mark.parametrize(
    'name, slug',
        [ 
        ('test_name_f', 'test_slug_f'),
        ('test_name_f', 'test_slug_f'),
    ],
)
def test_product_insert_data(db, category_factory, product_factory, name, slug):
    """Test product model creation with insert data"""

    category = category_factory.create(name='some_cat_name', slug='some_cat_slug')
    product = product_factory.create(name=name, slug=slug)

    assert product.name == name
    assert product.slug == slug
    

@pytest.mark.dbfixture
@pytest.mark.parametrize(
    'name, slug, store_price, retail_price',
        [ 
        ('test_name_f', 'test_slug_f', 92, 97),
        ('test_name_f', 'test_slug_f', 99, 107.65),
    ],
)
def test_product_inventiry_insert_data(db, product_inventory_factory, name, slug, store_price, retail_price):
    """Test product inventory model creation with insert data"""

    product_inventory = product_inventory_factory.create(
        name=name,
        slug=slug,
        store_price=store_price,
        retail_price=store_price
    )

    assert product_inventory.name == name
    assert product_inventory.slug == slug
    assert product_inventory.store_price == store_price
    assert product_inventory.store_price == store_price

