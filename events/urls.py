from django.contrib import admin
from django.urls import path, include
from events import views


urlpatterns = [
    #path('' views.get_habits, name = 'get_habits'),
    path('', views.landing, name = 'landing'),
]