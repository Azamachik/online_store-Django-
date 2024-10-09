from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from goods.forms import AddProductForm
from goods.models import Categories, Product


def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
    category = get_object_or_404(Categories, slug=cat_slug)
    products = Product.objects.filter(category_id=category.pk).select_related('category')

    data: dict = {'title': f'{category.name}',
                  'products': products,
                  'cat_selected': category.pk,
                  }
    return render(request, 'main/index.html', context=data)


def show_product(request: HttpRequest, product_slug) -> HttpResponse:
    product = get_object_or_404(Product, slug=product_slug)

    data = {
        'title': product.name,
        'product': product,
        'cat_selected': 1,
    }

    return render(request, 'goods/product.html', data)


def add_product(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            # try:
            #     print(form.cleaned_data)
            #     Product.objects.create(**form.cleaned_data)
            #     return redirect('main:home')
            # except Exception as error:
            #     print(error)
            #     form.add_error(None, 'Ошибка при добавлении товара')
            form.save()
            return redirect('main:home')

    else:
        form = AddProductForm()

    data = {
        'title': "Добавление товара",
        'form': form,
    }

    return render(request, 'goods/add_product.html', data)
