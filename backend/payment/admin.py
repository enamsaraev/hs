from django.contrib import admin

from payment.models import PaymentData


@admin.register(PaymentData)
class PaymentDataAdmin(admin.ModelAdmin):
    list_display = ('order', 'is_paid', 'order_is_paid')
    readonly_fields = ('payment_id', 'order', 'is_paid')

    @admin.display(ordering='order__is_paid', description='Заказ оплачен')
    def order_is_paid(self, obj):
        return 'Да' if obj.order.is_paid else 'Нет'

    def has_delete_permission(self, request, obj=None):
        return False