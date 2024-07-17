from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Информация', 'url_name': 'info'},
    {'title': 'Корзина', 'url_name': 'cart'},
    {'title': 'Войти', 'url_name': 'login'}
]

db = [
    {'id': 1, 'user_name': 'Azamat', 'is_authenticated': True},
    {'id': 2, 'user_name': 'Slava', 'is_authenticated': True},
    {'id': 3, 'user_name': 'Ratmir', 'is_authenticated': False},
    {'id': 4, 'user_name': 'Azaliya', 'is_authenticated': True},
    {'id': 5, 'user_name': 'Denis', 'is_authenticated': True}
]

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    data: dict = {'title': 'Главная страница',
                  'menu': menu,
                  'data': db,
                  }
    return render(request, 'main/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    data: dict = {'title': 'О сайте',
                  'menu': menu,
                  }
    return render(request, 'main/about.html', data)


def info(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Доп инфа')


def cart(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Корзина')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Авторизация')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
