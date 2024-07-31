from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Categories(MPTTModel):
    name = models.CharField(max_length=150, unique=True, verbose_name='Категория')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, blank=True, null=True,
                            related_name='children', db_index=True, verbose_name='Родительская категория')
    slug = models.SlugField(max_length=250, verbose_name='URL')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        db_table = 'category'
        unique_together = [['parent', 'slug']]
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('goods:category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    category = TreeForeignKey('Categories', on_delete=models.PROTECT, related_name='products', verbose_name='Категория')
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображения')
    price = models.DecimalField(default=0.00, max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    # seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('goods:product', kwargs={'product_slug': self.slug})

    def __str__(self):
        return self.name


# class Gallery(models.Model):
#     image = models.ImageField(upload_to='gallery')
#     product = TreeForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, related_name='images', verbose_name='Изображения')