from django.contrib import admin
from .models.Shop import Shop
from .models.Product import Product
from .models.Comment import Comment

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Comment)

# Register your models here.
