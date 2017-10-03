from django.http import HttpResponse
from django.shortcuts import render
from .models import Shop


def index(request):
    return HttpResponse("Congratulations! It is index page!")

def select_all(request):
    a = Shop.objects.all()
    list = []
    for i in a:
        list.append(i)
        list.append("<br>")
    return HttpResponse(list)
