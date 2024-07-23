from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


goods_db = [
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
    {
        'image': 'main/images/450x600.jpg',
        'name': 'Iphone 15 Pro Max Ultra +',
        'description': 'Очень очень при очень очень дорогой Iphone 15 Pro Max Ultra +',
        'price': 150,
    },
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
                  'cat_selected': 0,
                  'products': goods_db,
                  }
    return render(request, 'main/index.html', context=data)


def about(request: HttpRequest) -> HttpResponse:
    data: dict = {'title': 'О сайте',
                  }
    return render(request, 'main/about.html', data)


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
                  'products': goods_db,
                  'cat_selected': cat_id,
                  }
    return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
