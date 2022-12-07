from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

class Coupon(models.Model):
    """Coupon model"""
    
    code = models.CharField(
        max_length=50, 
        unique=True,
        blank=False,
        null=False,
        verbose_name=_('Код активации промокода'),
        help_text=_('Формат: обязательный, макс. длины - 50 символов')
    )
    valid_from = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name=_('Дата начала действия промокода'),
        help_text=_('Формат: обязательный')
    )
    valid_to = models.DateTimeField(
        blank=False,
        null=False,
        verbose_name=_('Дата окончания действия промокода'),
        help_text=_('Формат: обязательный')
    )
    count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name=_('Количество использования промокода'),
        help_text=_('Формат: необязательный')
    )
    discount = models.PositiveIntegerField(
        blank=False,
        null=False,
        verbose_name=_('% скидки'),
        help_text=_('Формат: обязательный, значение от 0%-100%'),
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если промокод используется'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если промокод не используется'),
        help_text=_('Формат: обязательный')
    )

    def get_count(self):
        return self.count

    def set_minus_count(self):
        """Minus count"""
        
        self.count -= 1
        self.save(update_fields=['count'])

    def __str__(self):
        return self.code
