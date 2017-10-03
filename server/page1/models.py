from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.TextField(default="Empty")
    adress = models.TextField(default="Empty")

    def __str__(self):
        return self.name + " " + self.adress

    class Meta:
        db_table = "shop"


class Product(models.Model):
    name = models.TextField(default="Empty")
    price = models.FloatField(default=0.0)
    shopFK = models.ForeignKey(Shop)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"


class Comment(models.Model):
    rate = models.IntegerField(default=0)
    commentLine = models.TextField(default="")
    shopFK = models.ForeignKey(Shop)

    def __str__(self):
        return self.commentLine

    class Meta:
        db_table = "comment"


