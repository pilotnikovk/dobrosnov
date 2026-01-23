from django.db import models
from django.urls import reverse
from .utils import compress_image

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL', default='default_slug')
    description = models.TextField(blank=True, verbose_name='Описание')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL', default='default_slug')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    sku = models.CharField(max_length=50, verbose_name='Артикул', unique=True, default='000000')
    short_description = models.TextField(verbose_name='Краткое описание', default='')
    full_description = models.TextField(verbose_name='Полное описание', default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Старая цена')
    image = models.ImageField(upload_to='products/', verbose_name='Основное изображение')
    image2 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Доп. изображение 1')
    image3 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Доп. изображение 2')
    image4 = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Доп. изображение 3')
    material = models.CharField(max_length=100, verbose_name='Материал', default='')
    dimensions = models.CharField(max_length=100, verbose_name='Размеры (Ш x Г x В)', default='0x0x0')
    weight = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Вес (кг)', default='0.00')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_id': self.id})
    
    def save(self, *args, **kwargs):
        if self.image and (not self.pk or Product.objects.get(pk=self.pk).image != self.image):
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(verbose_name='Email')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)], verbose_name='Рейтинг')
    text = models.TextField(verbose_name='Текст отзыва')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Отзыв на {self.product.name} от {self.author}'
