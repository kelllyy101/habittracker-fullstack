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
from habit import views as habit_views
from events import views as events_views
from users import views as users_views

from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', events_views.home, name="home"),
    path('events/', include('events.urls')),
    path('dashboard', habit_views.get_habits, name = 'get_habits'),
    path('add', habit_views.add_habit, name = 'add'),
    path('edit/<item_id>', habit_views.edit_habit, name='edit'),
    path('toggle/<item_id>', habit_views.toggle_habit, name='toggle'),
    path('delete/<item_id>', habit_views.delete_habit, name='delete'),
    path('login_user', users_views.login_user, name="login"),
    #path('logout_user', habit_views.logout_user, name='logout'),
    #path('register_user', habit_views.register_user, name='register_user'),
]
    # path('members/', include('django.contrib.auth.urls')),
    # path('members/', include('users.urls')),
 # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

