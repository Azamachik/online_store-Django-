from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Каталог', 'url_name': 'catalog'},
    {'title': 'Информация', 'url_name': 'info'},
    {'title': 'Новости', 'url_name': 'news'},
    {'title': 'Избранное', 'url_name': 'wishlist'},
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
cats_db = [
    {'id': 1, 'title': 'Телефоны'},
    {'id': 2, 'title': 'Планшеты'},
    {'id': 3, 'title': 'Телевизоры'},
    {'id': 4, 'title': 'Пылесосы'},
    {'id': 5, 'title': 'Холодильники'},
]
# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    data: dict = {'title': 'Главная страница',
                  'menu': menu,
                  'data': db,
                  'cat_selected': 0,
                  }
    return render(request, 'main/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    data: dict = {'title': 'О сайте',
                  'menu': menu,
                  }
    return render(request, 'main/about.html', data)


def catalog(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Каталог')


def wishlist(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Избранные товары')


def news(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Новости сайта')


def info(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Вся информация')


def cart(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Корзина')


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Авторизация')


def show_category(request: HttpRequest, cat_id: int) -> HttpResponse:
    data: dict = {'title': 'Отображение по категории',
                  'menu': menu,
                  'data': db,
                  'cat_selected': cat_id,
                  }
    return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
