from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField


class VariationManager(models.Manager):
    """Variation model manager"""

    def get_queryset(self):
        return super().get_queryset().all()

    def get_variation(self, product_slug, size, color):
        """"""
        variation = self.get_queryset().get(
            product=ProductInventory.objects.get(slug=product_slug),
            size=Size.objects.get(value=size),
            color=Color.objects.get(value=color)
        )

        return variation

class Category(MPTTModel):
    """Category model"""

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Имя категории товара'),
        help_text=_('Формат: обязательный, максимальная длина символов - 255')
    )
    slug = models.SlugField(
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        verbose_name=_('Путь до товаров этой категории'),
        help_text=_('Формат: обязательный, максимальная длина символов - 255')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если категория используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если категория должна быть удалена'),
        help_text=_('Формат: обязательный')
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
        related_name='children',
        null=True,
        blank=True,
        unique=False,
        verbose_name=_('Дочерняя категория'),
        help_text=_('Формат: необязательный'),
    )

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    """Product model"""

    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Имя типа товара'),
        help_text=_('Формат: обязательный, максимальная длина символов - 255')
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=False,
        unique=True,
        verbose_name=_('Путь до товаров этого типа'),
        help_text=_('Формат: обязательный, максимальная длина символов - 255, название такое же, как и у категории')
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Описание типа товара"),
        help_text=_("Формат: обязательный"),
    )
    category = TreeManyToManyField(
        Category,
        null=True,
        blank=True,
        verbose_name=_('Выбрать категорию к которой привязан данный тип товара'),
        help_text=_('Формат: обязательный')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если тип товара используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если тип товара должен быть удалена'),
        help_text=_('Формат: обязательный')
    )

    def __str__(self) -> str:
        return self.name

class Media(models.Model):
    """Media imges for the product"""

    img = models.ImageField(upload_to='img/')
    is_default = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если фото товара главное '),
        help_text=_('Формат: необязательный'))
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если фото товара используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если фото товара должно быть удалено'),
        help_text=_('Формат: обязательный')
    )

class ProductInventory(models.Model):
    """Some product model"""

    name = models.CharField(
        max_length=255, 
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_('Имя товара'),
        help_text=_('Формат: обязательный, максимальная длина - 255'),
    )
    slug = models.CharField(
        max_length=255, 
        null=False, 
        unique=False, 
        blank=False, 
        verbose_name=_('Путь до товара'),
        help_text=_('Формат: обязательный, максимальная длина - 255')
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
        related_name='product_inventory'
    )
    store_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Базовая стоимость товара"),
        help_text=_("Формат: число, максимальное значение - 99999.99"),
        error_messages={
            "name": {
                "max_length": _("Цена товара должна быть между 0 и 99999.99."),
            },
        },
    )
    retail_price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Цена продажи"),
        help_text=_("Формат: число, максимальное значение - 99999.99"),
        error_messages={
            "name": {
                "max_length": _("Цена товара должна быть между 0 и 99999.99."),
            },
        },
    )
    media = models.ManyToManyField(
        'Media',
        blank=True,
        null=True,
        verbose_name=_('Фото товара'),
        help_text=_('Связана с Медиа')
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Описание товара"),
        help_text=_("Формат: обязательный"),
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

class Size(models.Model):
    """Size models for the product"""

    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'XLARGE'),
    )
    value = models.CharField(
        max_length=20,
        choices=SIZE_CHOICES,
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_('Размер товара'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если размер товара используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если размер товара должен быть удален'),
        help_text=_('Формат: обязательный')
    )

    def __str__(self) -> str:
        return self.value


class Color(models.Model):
    """Color model for the product"""

    COLOR_CHOICES = (
        ('Black', 'Black'),
        ('White', 'White'),
    )
    value = models.CharField(
        max_length=25,
        choices=COLOR_CHOICES,
        null=True, 
        unique=False, 
        blank=True, 
        verbose_name=_('Цвет товара'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если цвет товара используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если цвет товара должен быть удален'),
        help_text=_('Формат: обязательный')
    )

    def __str__(self) -> str:
        return self.value


class Variation(models.Model):
    """Product variations model"""

    product = models.ForeignKey(
        ProductInventory, 
        on_delete=models.PROTECT, 
        related_name="variations"
    )
    size = models.ForeignKey(
        Size, 
        on_delete=models.CASCADE
    )
    color = models.ForeignKey(
        Color, 
        on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("Количество комбинации"),
        help_text=_("Формат: обязательный"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Выбрать, если вариация товара используется в каталоге'),
        help_text=_('Формат: обязательный')
    )
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_('Выбрать, если вариация товара должна быть удалена'),
        help_text=_('Формат: обязательный')
    )

    objects = VariationManager()


    class Meta:
        unique_together = ['color', 'size']
        ordering = ['size']

    def set_minus_count(self, qunatity):
        """Minus count"""
        
        self.count -= int(qunatity)
        self.save(update_fields=['count'])

    def __str__(self) -> str:
        return self.product.name