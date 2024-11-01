from django.contrib import admin
from django.utils.safestring import mark_safe
from . models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields={'slug':('name',)} 
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'created', 'available', 'discount')
    list_editable=('price', 'available', 'discount')
    prepopulated_fields={'slug':('name',)} 
    list_filter=('name', 'price')
    list_display_links=('name',)
    