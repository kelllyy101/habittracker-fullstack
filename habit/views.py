import json

from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ItemForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'events/templates/home.html')


@login_required
def get_habits(request):     
    items = Item.objects.filter(user_id=request.user.id).order_by('id')
    context = {
        'items': items
    }
    return render(request, 'habits/habits.html', context)


@login_required
def add_habit(request):
    if request.method == 'POST':
        form  = ItemForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            setattr(habit, "user_id", request.user.id)
            messages.success(request, 'Added Habit Successfully!')
            habit.save()
            
        else:
            messages.error(request, 'Failed to add habit. Please ensure the habit is valid.')
        return redirect('get_habits')

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'habits/add_habit.html', context)


@login_required
def edit_habit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form  = ItemForm(request.POST, instance=item)
        if form.is_valid():
            messages.success(request, 'Habit Successfully Edited!')
            form.save()
            return redirect('get_habits')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'habits/edit_habit.html', context)


@login_required
def delete_habit(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    messages.success(request, 'Habit Successfully Deleted!')
    return redirect('get_habits')


@login_required
def admin_view(request, item_id):
    return redirect('admin/')


@login_required
def tick_habit(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        item_id = body["id"]
        dof = body["dayOfWeek"]
        item = get_object_or_404(Item, id=item_id)
        dof_value = getattr(item, dof)
        setattr(item, dof, not dof_value)
        item.save(update_fields=[dof]) 
 
        return HttpResponse('')


# @login_required
# def clear(request):
#     items = Item.objects.filter(user_id=request.user.id)
#     dofs = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
#     for item in items:
#         for dof in dofs:
#             setattr(item, dof, False)
#         item.save(update_items=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

#     messages.success(request, 'Habits Successfully Cleared!')
#     return HttpResponse('')
