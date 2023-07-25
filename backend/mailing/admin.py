from django.contrib import admin
from django import forms
from django.contrib.admin.sites import site
from django.contrib.admin.widgets import ForeignKeyRawIdWidget

from mailing.models import EmailEntry, EmailSendAutomaticly, EmailSendTemplate
from mailing.tasks import send_mail_wia_admin_automaticly


class SerachOrderFieldForAutomticEmail(forms.ModelForm):
    class Meta:
        model = EmailSendAutomaticly
        widgets = {
            'email_order': ForeignKeyRawIdWidget(EmailSendAutomaticly._meta.get_field('email_order').remote_field, site),
        }
        fields = '__all__'


@admin.register(EmailEntry)
class EmailEntryAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('email',)
    search_fields = ('email',)
    list_filter = ('is_deleted',)
    readonly_fields = ('email', 'from_email', 'subject', 'text', 'template_name', 'is_sent', 'order',)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EmailSendAutomaticly)
class EmailSendAutomaticlyAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('email_order', 'subject', 'created_at')
    search_fields = ('email_order', 'subject', 'created_at')
    list_filter = ('is_deleted',)
    form = SerachOrderFieldForAutomticEmail

    def save_model(self, request, obj, form, change) -> None:
        if not obj.email_order and not obj.email_order.email:
            return

        super().save_model(request, obj, form, change)

        send_mail_wia_admin_automaticly.delay(
            email_id=obj.id,
            to=[obj.email_order.email],
            message=obj.text,
            subject=obj.subject,
        )

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(EmailSendTemplate)
class EmailSendTemplateAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('is_deleted',)
    readonly_fields = ('html_template',)

    def has_delete_permission(self, request, obj=None):
        return False