from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Shop, Product, Comment
from .serializers import ServerSealizerShop, ServerSealizerProduct
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


def index(request):
    return HttpResponse("Congratulations! It is index page!")


def select_all(request):
    shops = Shop.objects.all()
    serializer = ServerSealizerShop(shops, many=True)
    return JsonResponse(serializer.data, safe=False)


def select_shop_town(request, town):
    shops = ""


def select_product_from_shop(request, shopId):
    products = Product.objects.filter(shopFK=shopId)
    serializer = ServerSealizerProduct(products, many=True)
    return JsonResponse(serializer.data, safe=False)


def get_comment_to_shop(request, shop, rate, comment):
    c = ""


def update_comment(request, oldLine, newLine):
    c = ""


def delete_comment(request, line):
    c = ""


