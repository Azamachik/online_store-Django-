from django.urls import path, register_converter
from . import views
from . import converters

#register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('',  views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    path('info/', views.info, name='info'),
    path('login/', views.login, name='login'),
]