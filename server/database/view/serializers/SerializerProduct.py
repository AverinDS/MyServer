from rest_framework import serializers
from ..work_with_DB import Product


class SerializerProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'shopFK')
