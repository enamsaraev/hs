from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import ProductInventory, Variation, Size, Color
from coupon_api.models import Coupon


class Order(models.Model):
    """Order model"""

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
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если товар используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если товар должен быть удалена'),
        help_text=_('Формат: обязательный')
    )
    coupon = models.ForeignKey(
        Coupon,
        null=True,
        blank=True,
        related_name='orders',
        on_delete=models.CASCADE,
        verbose_name=_('Использованный при оплате купон'),
        help_text=_('Связан с категорий Купон')
    )
    coupon_discount = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name=_('Скидка по купону в %'),
        help_text=_('% взята из скидки Купона')
    )
    total_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Общая стоимость заказа"),
        help_text=_("Сформирована автоматически")
    )
    is_paid = models.BooleanField(
        default=False
    )

    def set_is_paid(self):
        """Set a paid order"""

        self.is_paid = True
        self.save(update_fields=['is_paid'])


class OrderItems(models.Model):
    """Current order items"""

    order = models.ForeignKey(
        Order,
        related_name='items',
        on_delete=models.PROTECT,
        verbose_name=_("Текущий заказ"),
        help_text=_("Сформирован автоматически")
    )
    product_variation = models.ForeignKey(
        Variation,
        related_name='current_order',
        on_delete=models.PROTECT,
        verbose_name=_("Вариации товара в текущем заказе"),
        help_text=_("Сформированы автоматически")
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name=_("Cтоимость товара в текущем заказе"),
        help_text=_("Сформирована автоматически")
    )
    qunatity = models.PositiveIntegerField(
        default=1,
        null=False,
        blank=False,
        verbose_name=_("Общее количество товара в текущем заказе"),
        help_text=_("Сформировано автоматически")
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        editable=True,
        verbose_name=_("Дата создания"),
        help_text=_("Определяется автоматически, возможно редактирование")
    )
    id_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если вариация товара в заказе должна быть удалена'),
        help_text=_('Формат: обязательный'),
    )

    def get_total_cost(self):
        """Return total item cost"""

        return str(self.price * self.qunatity)


    def __str__(self) -> str:
        return self.order.name

