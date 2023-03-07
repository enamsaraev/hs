from django.contrib import admin

from orders.models import Order, OrderItems


class ProductItemsInline(admin.TabularInline):
    """Product inventory tabular"""

    model = OrderItems
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Order admin model"""

    list_display = ('id', 'email',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('email',)
    inlines = [
        ProductItemsInline
    ]
