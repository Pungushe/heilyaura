from django.urls import reverse
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=150, unique=True, verbose_name="Название категории")
    slug=models.SlugField(unique=True, null=True, verbose_name="URL категории")
    
    def get_absolute_url(self):
        return reverse("frontpage:product_list_by_category",
            args=[self.slug])
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=["name"]
        indexes=[models.Index(fields=["name"])]
        db_table="categories"
        verbose_name="Категория"
        verbose_name_plural="Категории"

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", verbose_name="Категория")
    name=models.CharField(max_length=255, verbose_name="Название товара")
    slug=models.SlugField(unique=True, null=True, verbose_name="URL товара")
    image = models.ImageField(upload_to='products/%Y/%m/%d', verbose_name="Изображение", blank=True)
    description=models.TextField(default="Здесь скоро будет описание товара", verbose_name="Описание")
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    available=models.BooleanField(default=True, verbose_name="Доступен")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    discount=models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name="Скидка")
    
    
    def get_absolute_url(self):
        return reverse("frontpage:product_detail", 
            kwargs={"slug": self.slug})
    def __str__(self):
        return self.name
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount / 100, 2)
        return self.price
    
    class Meta:
        db_table="products"
        ordering=["name"]
        indexes=[
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created_at"])
        ]
        verbose_name="Товар"
        verbose_name_plural="Товары"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE, verbose_name="Товар")
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name="Изображение")
    
    def __str__(self):
        return f'{self.product.name} - {self.image.name}'
    