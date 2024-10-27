from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView, CreateView

from goods.forms import AddProductForm
from goods.models import Categories, Product


# def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
#     category = get_object_or_404(Categories, slug=cat_slug)
#     products = Product.objects.filter(category_id=category.pk).select_related('category')
#
#     data: dict = {'title': f'{category.name}',
#                   'products': products,
#                   'cat_selected': category.pk,
#                   }
#     return render(request, 'main/index.html', context=data)


class ShowCategory(ListView):
    model = Categories
    template_name = 'main/index.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 100

    def get_queryset(self):
        category = Categories.objects.get(slug=self.kwargs['cat_slug'])
        level_n = 1  # Уровень дочерних категорий, который вам нужен
        subclasses = category.get_children()
        for _ in range(level_n - 1):
            subclasses = [child for sub in subclasses for child in sub.get_children()]
        return Product.published.filter(category__in=subclasses).select_related('category')

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['products'][0].category
        context['title'] = category.name
        context['cat_selected'] = category.pk
        return context


# def show_product(request: HttpRequest, product_slug) -> HttpResponse:
#     product = get_object_or_404(Product, slug=product_slug)
#
#     data = {
#         'title': product.name,
#         'product': product,
#         'cat_selected': 1,
#     }
#
#     return render(request, 'goods/product.html', data)


class ProductDetail(DetailView):
    template_name = 'goods/product.html'
    context_object_name = 'product'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['product'].name
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Product.published, slug=self.kwargs[self.slug_url_kwarg])


# def add_product(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = AddProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             # try:
#             #     print(form.cleaned_data)
#             #     Product.objects.create(**form.cleaned_data)
#             #     return redirect('main:home')
#             # except Exception as error:
#             #     print(error)
#             #     form.add_error(None, 'Ошибка при добавлении товара')
#             form.save()
#             if "create_btn" in request.POST:
#                 return redirect('main:home')
#     else:
#         form = AddProductForm()
#
#     data = {
#         'title': "Добавление товара",
#         'form': form,
#     }
#
#     return render(request, 'goods/add_product.html', data)


class AddProduct(CreateView):
    template_name = 'goods/add_product.html'
    form_class = AddProductForm
    success_url = reverse_lazy('main:home')
    extra_context = {
        'title': "Добавление товара",
    }


class UpdateProduct(UpdateView):
    form_class = AddProductForm
    model = Product
    slug_url_kwarg = 'edit_slug'
    #fields = '__all__'
    template_name = 'goods/add_product.html'
    extra_context = {
        'title': "Редактирование товара",
    }


class DeleteProduct(DeleteView):
    #form_class = AddProductForm
    #model = Product
    slug_url_kwarg = 'delete_slug'
    context_object_name = 'product'
    #fields = '__all__'
    success_url = reverse_lazy('main:home')
    template_name = 'goods/delete_product.html'
    extra_context = {
        'title': "Удаление товара",
    }

    def get_queryset(self):
        return Product.published.all()
