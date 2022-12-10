import factory
import pytest
from pytest_factoryboy import register
from faker import Faker

from core import models
from orders.models import Order
from coupon_api.models import Coupon
from payment.models import PaymentData


fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    """Factory for the category model"""

    class Meta:
        model = models.Category

    name = factory.Sequence(lambda n: 'cat_name_{}'.format(n))
    slug = factory.Sequence(lambda n: 'cat_slug_{}'.format(n))


class ProductFactory(factory.django.DjangoModelFactory):
    """Factory for the product model"""

    class Meta:
        model = models.Product

    name = factory.Sequence(lambda n: 'prod_name_{}'.format(n))
    slug = factory.Sequence(lambda n: 'prod_slug_{}'.format(n))
    description = fake.text()
    is_active = True
    is_deleted = False

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        if extracted:
            for category in extracted:
                self.category.add(category)


class ProductInventoryFactory(factory.django.DjangoModelFactory):
    """Factory for the category db model"""

    class Meta:
        model = models.ProductInventory

    name = factory.Sequence(lambda n: 'prod_inv_name_{}'.format(n))
    slug = factory.Sequence(lambda n: 'prod_inv_slug_{}'.format(n))
    product = factory.SubFactory(ProductFactory)
    store_price = 92
    retail_price = 97
    description = fake.text()
    is_active = True
    is_deleted = False


class OrderFactory(factory.django.DjangoModelFactory):
    """Order factory model"""

    class Meta:
        model = Order

    name = factory.Sequence(lambda n: 'order_name_{}'.format(n))
    email = factory.Sequence(lambda n: 'order_name_{}_@mail.com'.format(n))
    phone = factory.Sequence(lambda n: '8800_{}'.format(n))
    coupon = None
    coupon_discount = 0
    total_price = 3000.09
    is_active = True
    is_deleted = False


class CouponFactory(factory.django.DjangoModelFactory):
    """Coupon model factory"""

    class Meta:
        model = Coupon

    code = factory.Sequence(lambda n: 'coupon_code_{}'.format(n))
    valid_from = '2022-11-20 22:14:18'
    valid_to = '2022-12-24 22:14:18'
    count = 10
    discount = 30
    is_active = True
    is_deleted = False


class PaymentDataFactory(factory.django.DjangoModelFactory):
    """Payment data model factory"""

    class Meta:
        model = PaymentData

    payment_id = factory.Sequence(lambda n: 'coupon_code_{}'.format(n))
    order = factory.SubFactory(OrderFactory)


register(CategoryFactory)
register(ProductFactory)
register(ProductInventoryFactory)
register(OrderFactory)
register(CouponFactory)
register(PaymentDataFactory)
