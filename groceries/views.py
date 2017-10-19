from django.shortcuts import render

from django.http import HttpResponse
from .models import Item


def index(request):
    grocery_list = Item.objects.order_by('name')
    return HttpResponse(grocery_list)