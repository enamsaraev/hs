from django.contrib import admin

from mailing.models import EmailEntry, EmailSendAutomaticly
from mailing.tasks import send_mail_wia_admin_automaticly


@admin.register(EmailEntry)
class EmailEntryAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('email',)
    search_fields = ('email',)


@admin.register(EmailSendAutomaticly)
class EmailSendAutomaticlyAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('recipient', 'subject',)
    search_fields = ('recipient', 'subject',)

    def save_model(self, request, obj, form, change) -> None:
        if not obj.recipient:
            return
        if not obj.subject:
            return
        if not obj.text:
            return

        send_mail_wia_admin_automaticly.delay(
            to=[obj.recipient],
            message=obj.text,
            subject=obj.subject,
            template_name=obj.template_name,
        )

        super().save_model(request, obj, form, change)

        