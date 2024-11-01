from django.db import models


class Product(models.Model):
    description = models.TextField(max_length=150)
    price = models.FloatField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    class Meta:
        verbose_name = 'Prodotto'
        verbose_name_plural = 'Prodotti'

    def __str__(self):
        return self.description

