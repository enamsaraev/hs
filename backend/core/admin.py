from django.contrib import admin

from core.models import Product, ProductInventory, Media, Variation, Size, Color


class VariationInline(admin.StackedInline):
    """Inline variations"""

    model = Variation
    extra = 1
    filter_horizontal = ('size', 'color',)


class MediaInline(admin.StackedInline):
    """Inline variations"""

    model = Media
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('is_deleted',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('is_deleted',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

    inlines = [MediaInline, VariationInline]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_filter = ('is_deleted',)
    search_fields = ('value',)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_filter = ('is_deleted',)
    search_fields = ('value',)

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('get_product_name',)
    list_filter = ('is_deleted',)
    search_fields = ('product.name',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(VariationAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['product'].label_from_instance = lambda inst: "{}".format(inst.name)
        return form

    def get_product_name(self, obj):
        return obj.product.name
    
    def has_delete_permission(self, request, obj=None):
        return False
    


