from django.contrib import admin

from mailing.models import EmailEntry, EmailSendAutomaticly, EmailSendTemplate
from mailing.tasks import send_mail_wia_admin_automaticly


@admin.register(EmailEntry)
class EmailEntryAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('email',)
    search_fields = ('email',)


@admin.register(EmailSendAutomaticly)
class EmailSendAutomaticlyAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('recipient', 'subject', 'created_at')
    search_fields = ('recipient', 'subject', 'created_at')

    def save_model(self, request, obj, form, change) -> None:
        if not obj.recipient:
            return
        if not obj.subject:
            return

        super().save_model(request, obj, form, change)

        send_mail_wia_admin_automaticly.delay(
            email_id=obj.id,
            to=[obj.recipient],
            message=obj.text,
            subject=obj.subject,
            template_name=obj.template_name,
        )


@admin.register(EmailSendTemplate)
class EmailEntryAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('name',)
    search_fields = ('name',)