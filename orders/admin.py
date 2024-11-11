from django.contrib import admin
from .models import Order, OrderItem 
from django.utils.safestring import mark_safe

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    
def order_stripe_payment(obj):
    url = obj.get_stripe_url()
    
    if obj.stripe_id:
        html = f'<a href="{url}" target="_blank">{obj.stripe_id}</a>'
        return mark_safe(html)
    return ''
order_stripe_payment.short_description = 'Оплата Stripe'
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'city', 'created_at', 'updated_at', 'paid', order_stripe_payment, 'email', 'address', 'postal_code']
    list_filter=['paid', 'created_at', 'updated_at']
    inlines = [OrderItemInline]