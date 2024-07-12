from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Главная страница</h1>')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>О нас!</h1>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def categrories_by_slug(request, cat_slug):
    print(request.POST)
    return HttpResponse(f'<h1>Товары по слагу: {cat_slug}')