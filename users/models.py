from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image=models.ImageField(upload_to="users_image", blank=True, null=True, verbose_name="Логотип")
    def __str__(self):
        return self.username
    
    class Meta:
        db_table="User"
        verbose_name="Пользователь"
        verbose_name_plural="Пользователи"
