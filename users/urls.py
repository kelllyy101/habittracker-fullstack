from django.urls import path
from . import views
from users import views as users_views

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register_user', users_views.register_user, name='register_user'),
    path('login/', users_views.login_user, name="login"),
    # path("login/", auth_views.LoginView.as_view()),
    path('logout_user', users_views.logout_user, name='logout'),
]