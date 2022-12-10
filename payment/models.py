from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class PaymentData(models.Model):
    """Payment data model"""

    payment_id = models.CharField(
        max_length=100
    )
    order = models.ForeignKey(
        Order,
        related_name='payment',
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    is_deleted = models.BooleanField(
        default=False
    )