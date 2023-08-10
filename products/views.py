from django.http import JsonResponse
from .models import Product


def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())}
    return JsonResponse(data)


