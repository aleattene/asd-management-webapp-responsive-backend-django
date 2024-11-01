from rest_framework import serializers
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

        extra_kwargs = {
            'description': {
                'help_text': 'Inserire una descrzione dettagliata del prodotto.'
            },
            'price': {
                'help_text': 'Inserire il prezzo del prodotto.'
            },
            # Other fields here if needed
        }

