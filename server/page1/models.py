from django.db import models

# Create your models here.
class shop(models.Model):
    name = models.TextField(default="Empty")
    adress = models.TextField(default="Empty")

    def __str__(self):
        return self.name +" "+ self.adress

    class Meta:
        db_table = "shop"

class product(models.Model):
    name = models.TextField(default="Empty")
    price = models.FloatField(default=0.0)
    shopFK = models.ForeignKey(shop)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "product"

