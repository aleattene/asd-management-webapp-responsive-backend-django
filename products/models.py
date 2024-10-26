from django.db import models


class Product(models.Model):
    description = models.TextField(max_length=150)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Prodotto'
        verbose_name_plural = 'Prodotti'

    def __str__(self):
        return self.description

