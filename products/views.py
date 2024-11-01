from django.views.generic import ListView, DetailView
from .models import Product


class ProductListView(ListView):
    """ Show all products """
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'
    ordering = ['price']


class ProductDetailView(DetailView):
    """ Show product details """
    model = Product
    template_name = 'products/products_detail.html'
    context_object_name = 'product'
