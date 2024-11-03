from django.urls import path, register_converter
from . import views
from . import converters

#register_converter(converters.FourDigitYearConverter, 'year4')

app_name = 'main'

urlpatterns = [
    path('',  views.HomePage.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('news/', views.news, name='news'),
    path('info/', views.info, name='info'),
]
