from django.shortcuts import render

# Create your views here.
def get_habits(request):
    return render(request, 'habits/habits.html')

