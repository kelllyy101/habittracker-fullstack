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
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    # path('', events_views.home, name="home"),
    # path('events/', include('events.urls')),
    path('', events_views.landing, name = ''),
    path('app', habit_views.get_habits, name = 'get_habits'),
    path('add', habit_views.add_habit, name = 'add'),
    path('edit/<item_id>', habit_views.edit_habit, name='edit'),
    path('tick', habit_views.tick_habit, name='tick'),
    path('toggle/<item_id>', habit_views.toggle_habit, name='toggle'),
    path('delete/<item_id>', habit_views.delete_habit, name='delete'),
    # path('', include('django.contrib.auth.urls')),
    path('', include('users.urls')),
]
#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
