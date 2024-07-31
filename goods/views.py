from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from goods.models import Categories, Product


# Create your views here.
# def catalog(request: HttpRequest) -> HttpResponse:
#     data = {
#         'title': 'Каталог',
#         'goods': [
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#             {
#                 'image': 'main/images/450x600.jpg',
#                 'name': 'Телефон',
#                 'description': 'Очень дорогой телефон',
#                 'price': 150,
#             },
#         ]
#     }
#     return render(request, 'goods/catalog.html', context=data)

def show_category(request: HttpRequest, cat_slug: str) -> HttpResponse:
    category = get_object_or_404(Categories, slug=cat_slug)
    products = Product.objects.filter(category_id=category.pk)

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