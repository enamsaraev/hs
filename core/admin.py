from django.contrib import admin

from core.models import Category, Product, ProductInventory, Media, Variation, Size, Color


class VariationInline(admin.StackedInline):
    """Inline variations"""

    model = Variation
    extra = 3


class MediaInline(admin.StackedInline):
    """Inline variations"""

    model = Media
    extra = 3


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('name',)


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('name',)

    inlines = [MediaInline, VariationInline]


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('value',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('value',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('value',)


@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ('get_product_name',)
    list_filter = ('is_deleted', 'is_active',)
    search_fields = ('product',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(VariationAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['product'].label_from_instance = lambda inst: "{}".format(inst.name)
        return form

    def get_product_name(self, obj):
        return obj.product.name
    


