from django.shortcuts import render
from .models import Item
from django.shortcuts import render, redirect

# Create your views here.


def get_habits(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'habits/habits.html', context)

def add_habit(request):
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_habits')

    return render(request, 'habits/add_habit.html')