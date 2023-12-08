"""habit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from habit import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_habits, name = 'get_habits'),
    path('add', views.add_habit, name = 'add'),
    path('edit/<item_id>', views.edit_habit, name='edit'),
    path('toggle/<item_id>', views.toggle_habit, name='toggle'),
    path('delete/<item_id>', views.delete_habit, name='delete'),
    # path('members/', include('django.contrib.auth.urls')),
    # path('members/', include('users.urls')),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

