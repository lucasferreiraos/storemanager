from django.contrib import admin
from .models import Product


class Products(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'price', 'units',)
    list_display_links = ('id', 'name',)
    search_fields = ('name', 'brand')


admin.site.register(Product, Products)
