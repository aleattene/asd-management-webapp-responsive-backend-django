from rest_framework import viewsets
from products.models import Product
from products.api.serializers import ProductSerializer
from core.permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


