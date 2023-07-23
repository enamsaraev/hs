from django.contrib import admin

from coupon_api.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'valid_from', 'valid_to', 'discount', 'is_active',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('code',)

    def has_delete_permission(self, request, obj=None):
        return False
