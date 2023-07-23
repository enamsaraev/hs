from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class PaymentData(models.Model):
    """Payment data model"""

    payment_id = models.CharField(
        max_length=100,
        verbose_name=_("ID оплаченного платежа за заказ"),
        help_text=_("Создается автоматически"),
    )
    order = models.ForeignKey(
        Order,
        related_name='payment',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Заказ"),
        help_text=_("Создается автоматически"),
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name=_("Галочка стоит, если заказ оплачен"),
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Выбрать, если нужно удалить"),
    )

    class Meta:
        verbose_name = 'ID заказа'
        verbose_name_plural = 'ID заказов'

    def __str__(self) -> str:
        return self.payment_id
    
    def set_is_paid(self):
        """Set a paid order"""

        self.is_paid = True
        self.save(update_fields=['is_paid'])