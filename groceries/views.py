from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Item


def index(request):
    grocery_list = Item.objects.order_by('name')
    template = loader.get_template('items/index.html')
    context = {
        'grocery_list': grocery_list
    }
    return HttpResponse(template.render(context, request))