from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('product/', views.show_product, name='product'),
]