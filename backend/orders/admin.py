from django.contrib import admin

from orders.models import Order, OrderItems
from mailing.models import EmailSendAutomaticly


class ProductItemsInline(admin.TabularInline):
    """Product inventory tabular"""

    model = OrderItems
    extra = 0


class EmailSendAutomaticlyItemsInline(admin.TabularInline):
    model = EmailSendAutomaticly
    extra = 1
    

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('id', 'email',)
    list_filter = ('is_deleted',)
    search_fields = ('email',)
    inlines = [
        ProductItemsInline,
        EmailSendAutomaticlyItemsInline
    ]
