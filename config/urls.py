from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Корзина
    path('cart/', include('cart.urls', namespace='cart')),
    # Пользователя
    path('users/', include('users.urls', namespace='users')),
    # Заказы
    path('orders/', include('orders.urls', namespace='orders')),
    # Оплата
    path('payment/', include('payment.urls', namespace='payment')),
    # Главная страница
    path('', include('frontpage.urls', namespace='frontpage')),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
