from django import forms
from .models import Item


class ItemForm(forms.ModelForm): 
    class Meta:
        model = Item
        fields = ['name', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
