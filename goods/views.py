from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


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


def show_product(request: HttpRequest, cat_id) -> HttpResponse:
    return render(request, 'goods/product.html')