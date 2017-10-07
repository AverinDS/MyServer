from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Shop
from .serializers import ServerSealizerShop
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



def index(request):
    return HttpResponse("Congratulations! It is index page!")

def select_all(request):
    shops = Shop.objects.all()
    serializer = ServerSealizerShop(shops, many=True)
    return JsonResponse(serializer.data, safe=False)
