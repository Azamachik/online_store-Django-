from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Categories, Product
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "product_image", "created_at", "is_published", "category")
    list_display_links = ("name", )
    list_editable = ('is_published', )
    list_per_page = 30
    ordering = ("name", "created_at", "category")
    actions = ("set_published", "set_draft")
    search_fields = ("name__startswith", "category__name")
    list_filter = ("category__name", "is_published")
    readonly_fields = ('product_image', )
    fields = ('name', 'slug', 'description', 'price', 'quantity', 'discount', 'category', 'image', 'product_image',)
    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Product.Status.PUBLISHED)
        self.message_user(request, f"Изменено {count} записей")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Product.Status.DRAFT)
        self.message_user(request, f"{count} записей снято с публикации", messages.WARNING)

    @admin.display(description='Изображения')
    def product_image(self, product: Product):
        if product.image:
            return mark_safe(f"<img src='{product.image.url}' width=50")
        else:
            return "Без фото"
@admin.register(Categories)
class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
