from django.contrib import admin

from orders.models import Order, OrderItems
from mailing.models import EmailSendAutomaticly
from mailing.tasks import send_mail_wia_admin_automaticly


class ProductItemsInline(admin.TabularInline):
    """Product inventory tabular"""

    model = OrderItems
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('id', 'email', 'is_paid',)
    list_filter = ('is_deleted', 'is_paid',)
    search_fields = ('email', 'is_paid',)
    readonly_fields = ('name', 'email', 'phone', 'address', 'delivery_price', 'created_at', 'coupon', 'coupon_discount', 'total_price', 'is_paid',)
    inlines = [
        ProductItemsInline
    ]

    def has_delete_permission(self, request, obj=None):
        return False
