from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, FormView
from django.core.mail import send_mail
from goods.models import Product, Categories
from main.forms import ContactForm
from onlinestore.settings import DEFAULT_FROM_EMAIL


# Create your views here.
# def index(request: HttpRequest) -> HttpResponse:
#     products = Product.objects.all().select_related('category')
#     data: dict = {'title': 'Главная',
#                   'cat_selected': 0,
#                   'products': products,
#                   }
#     return render(request, 'main/index.html', context=data)


class HomePage(ListView):
    template_name = 'main/index.html'
    context_object_name = 'products'
    extra_context = {
        'title': 'Главная',
        'cat_selected': 0,
    }
    paginate_by = 100

    def get_queryset(self):
        return Product.published.all().select_related('category')
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Главная'
    #     context['cat_selected'] = 0
    #     context['products'] = Product.objects.all().select_related('category')
    #     return context


# @login_required
# def about(request: HttpRequest) -> HttpResponse:
#     data: dict = {'title': 'О сайте',
#                   }
#     return render(request, 'main/contact_form.html', data)
#

class ContactFormView(FormView):
    template_name = 'main/contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('main:home')
    extra_context = {'title': 'Обратная связь'}

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        #print(form.cleaned_data)
        #cd = form.cleaned_data
        #send_mail(cd['name'], cd['content'], cd['email'], [DEFAULT_FROM_EMAIL])
        return super().form_valid(form)

@login_required
def wishlist(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Избранные товары')


def news(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Новости сайта')


def info(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Вся информация')


@login_required
def cart(request: HttpRequest) -> HttpResponse:
    return HttpResponse('Корзина')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
