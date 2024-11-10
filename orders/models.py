from django.db import models
from frontpage.models import Product
from users.models import User


class Order(models.Model):
     user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None, verbose_name="Пользователь")
     first_name = models.CharField(max_length=50, verbose_name="Имя")
     last_name = models.CharField(max_length=50, verbose_name="Фамилия")
     email = models.EmailField(verbose_name="Электронная почта")
     city= models.CharField(max_length=50, verbose_name="Город")
     address = models.CharField(max_length=250, verbose_name="Адрес")
     postal_code = models.CharField(max_length=20, verbose_name="Почтовый индекс")
     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
     updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
     paid=models.BooleanField(default=False, verbose_name="Оплачен")
     

     def __str__(self):
          return f'Заказ {self.first_name} {self.last_name}'
     
     def get_total_cost(self):
          return sum(item.get_cost() for item in self.items.all())
     class Meta:
          db_table="order"
          ordering = ['-created_at']
          indexes = [
               models.Index(fields=['-created_at']),
          ]
          verbose_name = 'Заказ'
          verbose_name_plural = 'Заказы'
     
class OrderItem(models.Model):
     order = models.ForeignKey(to=Order, on_delete=models.CASCADE, related_name='items', verbose_name="Заказ")
     product = models.ForeignKey(Product,  on_delete=models.CASCADE, related_name='order_items', verbose_name="Продукт")
     price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
     quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
     
     def __str__(self):
          return str(self.order)
     
     def get_cost(self):
          return self.price * self.quantity
     
     class Meta:
          db_table="order_items"
          verbose_name = 'Заказ'
          verbose_name_plural = 'Заказы'
     
     
     