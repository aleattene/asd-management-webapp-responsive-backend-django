from rest_framework import viewsets
from products.models import Product
from products.api.serializers import ProductSerializer
from config.permissions import IsAdminOrReadOnly


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    queryset = Product.objects.all().order_by('price')
    serializer_class = ProductSerializer
    # renderer_classes = [CustomBrowsableAPIRenderer, JSONRenderer]


