from django.shortcuts import render, redirect
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Item
from groceries.forms import ItemForm

def new(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return HttpResponseRedirect('/items/new/')
    else:
        form = ItemForm()
        return render(request, 'items/new.html', 
            {'form': form,}
        )

class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/item-detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context


class ItemListView(ListView):
    template_name = 'items/index.html'
    model = Item
    context_object_name = 'items'

    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        context['name'] = self.model.name
        return context

