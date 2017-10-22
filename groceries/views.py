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
    form_class = ItemForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            item_name = request.POST.get('item_name', '')

            template = get_template('items/new.html')
            context = {'item_name': item_name}
            content = template.render(context)

    return render(request, 'items/new.html', 
        {'form': form_class,}
    )