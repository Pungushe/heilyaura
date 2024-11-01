from django.urls import path
from .views import *

app_name = 'frontpage'

urlpatterns = [
    path('', popular_list, name='popular_list'),
    path('shop/', product_list, name='product_list'),
    path('shop/<slug:slug>/', product_detail,
          name='product_detail'),
    path('shop/category/<slug:category_slug>/', product_list,
          name='product_list_by_category'),
]
