from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="80" />'.format(object.featured_image.url))

    thumbnail.short_description = 'Product image'

    list_display = ('id', 'thumbnail', 'name', 'price', 'category', 'in_stock')
    list_display_links = ('thumbnail', 'name')
    list_editable = ('price', 'category', 'in_stock')
    search_fields = ('name',)
    list_filter = ('category', 'in_stock')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
