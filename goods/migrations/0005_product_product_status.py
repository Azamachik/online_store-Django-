# Generated by Django 5.1 on 2024-10-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.IntegerField(choices=[(0, 'Б/y'), (1, 'Новое')], default=0, verbose_name='Состояние товара'),
        ),
    ]