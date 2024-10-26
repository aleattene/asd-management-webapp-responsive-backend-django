from django.shortcuts import get_object_or_404
from rest_framework import mixins, generics

from ..models import Product
from .serializers import ProductSerializer


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

