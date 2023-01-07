from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order

class EmailEntry(models.Model):
    """Email logging"""

    email = models.CharField(
        max_length=255, 
        null=False,
        verbose_name=_("Почта клиента, оформившего и купившего товары (заказ)"),
        help_text=_("Формат: обязательный"),
    )
    message = models.TextField(
        verbose_name=_("Текст сообщения"),
        help_text=_("Формат: обязательный"),
    )
    order = models.ForeignKey(
        Order,
        related_name='emails',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_("Текущий заказ клиента"),
        help_text=_("Формат: обязательный"),
    )

    def __str__(self):
        return self.email


class EmailSendAutomaticly(models.Model):
    """Text templates for an email"""

    recipient = models.EmailField(
        verbose_name=_("Почта для отправки смс покупателю"),
        help_text=_("Формат: обязательный"),
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_("Шапка смс для отправки почты покупателю"),
        help_text=_("Формат: обязательный"),
    )
    text = models.TextField(
        verbose_name=_("Текст смс для отправки почты покупателю"),
        help_text=_("Формат: обязательный"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Нажать, если нужно удалить шаблон"),
        help_text=_("Формат: обязательный"),
    )

    def __str__(self) -> str:
        return self.recipient
