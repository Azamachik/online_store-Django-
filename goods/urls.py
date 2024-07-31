from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('product/<slug:product_slug>/', views.show_product, name='product'),
]