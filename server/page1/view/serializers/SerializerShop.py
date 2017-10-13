from rest_framework import serializers
from ..work_with_DB import Shop


class SerializerShop(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'adress')
