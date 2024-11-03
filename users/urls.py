from django.urls import path
#from django.contrib.auth.views import LogoutView
from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    #path('logout/', LogoutView.as_view(next_page='main:home'), name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]
