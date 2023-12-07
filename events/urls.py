from django.contrib import admin
from django.urls import path, include
from habit import views


urlpatterns = [
    path('', views.get_habits, name = 'get_habits'),
]