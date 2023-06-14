from django.contrib import admin

from app.models import Product, Category, ProductImage


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    fields = ('name', 'parent', 'slug')


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'category', 'short_description', 'price', 'is_premium', 'shopping_cost', 'specification',
        'discount', 'quantity')
    fields = (
        'name', 'category', 'short_description', 'price', 'is_premium', 'description', 'shopping_cost', 'specification',
        'discount', 'quantity')


@admin.register(ProductImage)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
    fields = ('product', 'image')
