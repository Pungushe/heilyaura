from django.contrib import admin
from . models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)
    prepopulated_fields={'slug':('name',)} 
    
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 5
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'created_at', 'available', 'discount')
    list_editable=('price', 'available', 'discount')
    prepopulated_fields={'slug':('name',)} 
    list_filter=('name', 'price')
    list_display_links=('name',)
    inlines=[ProductImageInline]
    