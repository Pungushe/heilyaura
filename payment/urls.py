from django.urls import path
from .views import *
from . import webhooks

app_name = 'payment'

urlpatterns = [
     path('process/', payment_process, name='process'),    
     path('completed/', payment_completed, name='completed'),    
     path('canceled/', payment_canceled, name='canceled'),    
     path('stripe_webhook/', webhooks.stripe_webhook, name='stripe_webhook'),    
]
