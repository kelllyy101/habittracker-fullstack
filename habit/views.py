from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.shortcuts import render, redirect
from .forms import ItemForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from .forms import RegisterUserForm

# Create your views here.
def home(request):
    return render(request, 'events/templates/home.html')


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


def edit_habit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form  = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_habits')
    form = ItemForm(instance=item)
    context = {
'form': form
    }
    return render(request, 'habits/edit_habit.html', context)

def toggle_habit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('get_habits')

def delete_habit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_habits')


