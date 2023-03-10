from django.db import models
from django.utils.translation import gettext_lazy as _

from orders.models import Order


class EmailSendTemplate(models.Model):
    """HTML email templates"""

    name = models.CharField(
        max_length=255,
        verbose_name=_('Имя шаблона'),
        help_text=_('Обязательный, принимает текст'),
    )
    html_template = models.TextField(
        verbose_name=_('HTML код сообщения'),
        help_text=_('Обязательный, принимает html code'),
    )

    class Meta:
        verbose_name = 'Шаблоны кастомных имейлов'

    def __str__(self) -> str:
        return self.name


class EmailEntry(models.Model):
    """Email logging"""

    email = models.EmailField(
        max_length=200,
        verbose_name=_('Получать сообщения'),
        help_text=_('Обязательный, принимать ТОЛЬКО имейл'),
    )
    from_email = models.EmailField(
        max_length=200,
        verbose_name=_('Отправитель сообщения'),
        help_text=('Обязательный, по дефолту хранит хоста от почты'),
        default=''
    )
    subject = models.CharField(
        max_length=255,
        verbose_name=_('Тема сообщения'),
        help_text=_('Обязательный, принимает текст'),
    )
    text = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Текст письма'),
        help_text=_('Обязательный, принимает текст'),
    )
    template_name = models.TextField(
        blank=True,
        null=True,
        verbose_name=_('Имя шаблона письма'),
        help_text=_('Название шаблона'),
    )
    is_sent = models.BooleanField(
        default=True
    )
    order = models.ForeignKey(
        Order,
        related_name='emails',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name=_('Текущий заказ клиента'),
        help_text=_('Формат: обязательный'),
    )

    class Meta:
        verbose_name = 'Отправленный имейл при оформлении заказа'
        verbose_name_plural = 'Отправленные имейлы при оформлении заказа'

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
    template = models.ForeignKey(
        EmailSendTemplate,
        related_name='auto_emails',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_('Имя шаблона письма'),
        help_text=_('Название шаблона'),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(
        default=False,
        verbose_name=_("Нажать, если нужно удалить шаблон"),
        help_text=_("Формат: обязательный"),
    )
    deliered = models.BooleanField(
        default=False,
        verbose_name=_("Галочка стоит, если имейл доставлен"),
    )
    class Meta:
        verbose_name = 'Отправить имейл рассылку'
        verbose_name_plural = 'Отправить имейл рассылку'

    def __str__(self) -> str:
        return self.recipient
