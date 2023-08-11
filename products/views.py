from django.http import JsonResponse
from .models import Product


def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values())}
    return JsonResponse(data)


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "id": product.id,
            "description": product.description,
            "price": product.price,
            "active": product.active
        }}
    except Product.DoesNotExist:
        data = {"error": {
            "code": 404,
            "message": "Product not found!"
        }}
    return JsonResponse(data)


