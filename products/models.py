from django.db import models


class Product(models.Model):
    description = models.TextField(max_length=150)
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.description

