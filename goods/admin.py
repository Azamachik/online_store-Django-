from django.contrib import admin, messages
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Categories, Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ["id", "name", "created_at", "is_published", "category"]
    list_display_links = ["id", "name"]
    list_editable = ('is_published', )
    list_per_page = 30
    ordering = ("name", "created_at", "category")
    actions = ("set_published", "set_draft")
    search_fields = ("name__startswith", "category__name")
    list_filter = ("category__name", "is_published")

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Product.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Product.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)


@admin.register(Categories)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
