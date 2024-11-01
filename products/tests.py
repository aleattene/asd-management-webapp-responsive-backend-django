from django.test import TestCase
from django.urls import reverse
from .models import Product


class ProductViewsTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            description='Test Product',
            price=19.99,
            available=True
        )

    def test_product_list_view(self):
        url = reverse('products:products-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        self.assertTemplateUsed(response, 'products/products_list.html')

    def test_product_detail_view(self):
        url = reverse('products:products-detail', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Product')
        # self.assertContains(response, '€19.99')
        self.assertTemplateUsed(response, 'products/products_detail.html')

    def test_product_detail_view_not_found(self):
        url = reverse('products:products-detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
