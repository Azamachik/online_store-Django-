from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginUserForm, RegisterUserForm


# Create your views here.


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             user = authenticate(request, username=form.cleaned_data['username'],
#                                 password=form.cleaned_data['password'])
#             if user and user.is_active:
#                 login(request, user)
#                 return HttpResponseRedirect(reverse('main:home'))
#     else:
#         form = LoginUserForm()
#
#     return render(request, 'users/login.html', {'form': form})
#

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}


class RegisterUser(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')

# def register(request):
#     if request.method == 'POST':
#         form = RegisterUserForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#
#             return render(request, 'users/login.html', {'form': form})
#     else:
#         form = RegisterUserForm()
#     return render(request, 'users/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))
