from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from goods.models import Product, Categories


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all().select_related('category')
    data: dict = {'title': 'Главная',
                  'cat_selected': 0,
                  'products': products,
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


# def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
#     category = get_object_or_404(Categories, slug=cat_slug)
#     products = Product.objects.filter(category_id=category.pk)
#
#     data: dict = {'title': f'{category.name}',
#                   'products': products,
#                   'cat_selected': category.pk,
#                   }
#     return render(request, 'main/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
