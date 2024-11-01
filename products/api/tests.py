from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from ..models import Product


class ProductListCreateApiViewTest(APITestCase):
    def test_get_products_list(self):
        # Create two test-products
        Product.objects.create(description="Prodotto1", price=10.0)
        Product.objects.create(description="Prodotto2", price=15.0)

        # Call the reverse function to get the URL of the products-list view
        url = reverse('products-api-list')
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data contains the two products
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['description'], "Prodotto1")
        self.assertEqual(response.data[0]['price'], 10.0)
        self.assertEqual(response.data[1]['description'], "Prodotto2")
        self.assertEqual(response.data[1]['price'], 15.0)

