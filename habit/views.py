from django.shortcuts import render
from .models import Item
from django.shortcuts import render, redirect
from .forms import ItemForm

# Create your views here.


def get_habits(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'habits/habits.html', context)

def add_habit(request):
    if request.method == 'POST':
        form  = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_habits')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'habits/add_habit.html', context)


