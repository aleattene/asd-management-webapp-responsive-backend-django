from django.urls import path
from .views import ProductListCreateApiView, ProductDetailApiView

urlpatterns = [
    path('products/', ProductListCreateApiView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailApiView.as_view(), name='product-detail')
]