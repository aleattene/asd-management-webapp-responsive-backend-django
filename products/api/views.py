from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from products.api.renderers import CustomBrowsableAPIRenderer
from products.models import Product
from products.api.serializers import ProductSerializer
from core.permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer
    # renderer_classes = [CustomBrowsableAPIRenderer, JSONRenderer]


