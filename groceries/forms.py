from django import forms

from .models import Item

class ItemForm(forms.Form):
    item_name = forms.CharField(required=True)

    class Meta:
        model = Item
        fields = ('name',)