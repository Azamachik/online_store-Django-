from django.urls import path
from . import views

app_name = 'goods'

urlpatterns = [
    path('category/<slug:cat_slug>/', views.ShowCategory.as_view(), name='category'),
    path('product/<slug:product_slug>/', views.ProductDetail.as_view(), name='product'),
    path('addproduct/', views.AddProduct.as_view(), name='add_product'),
    path('edit/<slug:edit_slug>/', views.UpdateProduct.as_view(), name='edit_product'),
    path('delete/<slug:delete_slug>/', views.DeleteProduct.as_view(), name='delete_product'),
]
