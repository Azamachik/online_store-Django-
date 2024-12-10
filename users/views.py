from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, PasswordChangeUserForm


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
    template_name = 'users/users.html'
    links = {'Забыли пароль?': 'users:password_reset', 'Регистрация': 'users:register'}
    extra_context = {'title': "Авторизация", 'button': 'Войти', 'extra_links': links}


class RegisterUser(CreateView):
    template_name = 'users/users.html'
    form_class = RegisterUserForm
    extra_context = {'title': 'Регистрация', 'button': 'Зарегистрироваться'}
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


class ProfileUser(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    model = get_user_model()
    template_name = 'users/profile.html'
    extra_context = {'title': 'Личный кабинет'}

    def get_success_url(self):
        return reverse('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

# def logout_user(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('main:home'))


class PasswordChangeUser(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/users.html'
    form_class = PasswordChangeUserForm
    success_url = reverse_lazy('users:password_change_done')
    links = {'Забыли пароль?': 'users:password_reset'}
    extra_context = {'title': 'Изменение пароля', 'button': 'Изменить пароль', 'button2': 'Вернуться в профиль', 'extra_links': links}