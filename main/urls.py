from django.urls import path, register_converter
from . import views
from . import converters

#register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('',  views.index, name='index'),
    path('about/', views.about, name='about'),
    path('cats/<slug:cat_slug>/', views.categrories_by_slug)
    #path('archive/<year4: year>', views.archive),
]