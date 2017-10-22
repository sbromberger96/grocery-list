from django.shortcuts import render
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse
from django.template import loader

from .models import Item
from groceries.forms import ItemForm

def items(request):
    grocery_list = Item.objects.order_by('name')
    context = {'grocery_list': grocery_list}
    return render(request, 'items/index.html', context)

def new(request):
    if request.method == 'POST':
        form = ItemForm
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
        else:
            form = ItemForm()

    return render(request, 'items/new.html', 
        {'form': form,}
    )