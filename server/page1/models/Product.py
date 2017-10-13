from django.db import models
from .Shop import Shop


class Product(models.Model):
    name = models.TextField(default="Empty")
    price = models.FloatField(default=0.0)
    shopFK = models.ForeignKey(Shop)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"
