from django.contrib import admin

from mailing.models import EmailEntry, EmailSendAutomaticly, EmailSendTemplate
from mailing.tasks import send_mail_wia_admin_automaticly


@admin.register(EmailEntry)
class EmailEntryAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('email',)
    search_fields = ('email',)
    list_filter = ('is_deleted',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EmailEntryAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['order'].label_from_instance = lambda inst: "{}".format(inst.name)
        return form


@admin.register(EmailSendAutomaticly)
class EmailSendAutomaticlyAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('recipient', 'subject', 'created_at')
    search_fields = ('recipient', 'subject', 'created_at')
    list_filter = ('is_deleted',)

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
            template=obj.template.name,
        )


@admin.register(EmailSendTemplate)
class EmailSendTemplateAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('is_deleted',)