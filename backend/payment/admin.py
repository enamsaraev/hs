from django.contrib import admin

from payment.models import PaymentData


@admin.register(PaymentData)
class PaymentDataAdmin(admin.ModelAdmin):
    list_display = ('order', 'is_paid')
    readonly_fields = ('payment_id', 'order', 'is_paid')

    def has_delete_permission(self, request, obj=None):
        return False