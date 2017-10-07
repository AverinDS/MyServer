from rest_framework import serializers
from .models import Shop, Product, Comment


class ServerSealizerShop(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'adress')