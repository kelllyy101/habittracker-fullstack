from django.urls import path
from . import views
from users import views as users_views


urlpatterns = [
    path('register_user', users_views.register_user, name='register_user'),
    path('login_user', users_views.login_user, name="login"),
    path('logout_user', users_views.logout_user, name='logout'),
]