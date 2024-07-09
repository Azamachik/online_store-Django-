from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>Главная страница</h1>')


def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse('<h1>О нас!</h1>')