from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    class UserType(models.TextChoices):
        ADMIN = 'admin', 'админ'
        CUSTOMER = 'customer', 'покупатель'
        SELLER = 'seller', 'продавец'

    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True,
                              null=True, verbose_name='Фотография')
    birth_date = models.DateTimeField(blank=True, null=True, verbose_name='Дата рождения')
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    user_type = models.CharField(max_length=15, default=UserType.CUSTOMER, choices=UserType.choices, verbose_name='Роль')
