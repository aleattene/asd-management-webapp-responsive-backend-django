from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    """ Show all products """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    """ Show product details """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
