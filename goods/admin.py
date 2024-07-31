from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Categories, Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Categories)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}


