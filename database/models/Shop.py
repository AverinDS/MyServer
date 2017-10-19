from django.db import models


class Shop(models.Model):
    name = models.TextField(default="Empty")
    adress = models.TextField(default="Empty")

    def __str__(self):
        return self.name + " " + self.adress

    class Meta:
        db_table = "shop"
