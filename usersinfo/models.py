from django.db import models
from django.utils.translation import gettext_lazy as _
from orders.models import Order


class CustomerInfo(models.Model):
    """Info about all customers"""

    name = models.CharField(
        max_length=255, 
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_('Имя покупателя'),
        help_text=_('Формат: обязательный, максимальная длина - 255'),
    )
    email = models.EmailField(
        max_length=255, 
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_('Почта покупателя'),
        help_text=_('Формат: обязательный, максимальная длина - 255'),
    )
    phone = models.CharField(
        max_length=255, 
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_('Номер покупателя'),
        help_text=_('Формат: обязательный, максимальная длина - 255'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        editable=True,
        verbose_name=_("Дата создания"),
        help_text=_("Определяется автоматически, возможно редактирование")
    )
    order = models.ManyToManyField(
        Order
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если товар должен быть удалена'),
        help_text=_('Формат: обязательный')
    )
