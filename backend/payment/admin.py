from django.contrib import admin

from payment.models import PaymentData


@admin.register(PaymentData)
class PaymentDataAdmin(admin.ModelAdmin):
    list_display = ('get_order_name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(PaymentDataAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['order'].label_from_instance = lambda inst: "{}".format(inst.name)
        return form

    def get_order_name(self, obj):
        return obj.order.name