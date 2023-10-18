from django.contrib import admin
from django.utils.safestring import mark_safe

from create_item.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['type', 'slug']
    prepopulated_fields = {'slug': ('type',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'image_show', 'available', 'price', 'size']
    list_filter = ['available']
    list_editable = ['price', 'size', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'

    image_show.__name__ = 'Image'



