from rest_framework import serializers
from .models import Shop, Product, Comment


class ServerSealizerShop(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'adress')


class ServerSealizerProduct(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'shopFK')


class ServerSealizerComment(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'rate', 'commentLine', 'shopFK')