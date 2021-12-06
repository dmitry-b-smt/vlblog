from django.urls import path
from . import views
from django.contrib.auth import views as authViews
from .forms import LoginForm


urlpatterns = [
    path('registration', views.register, name='registration'),
    path('profile', views.profile, name='profile'),
    path('change_password', views.change_password, name='change_password'),
    path('user', authViews.LoginView.as_view(template_name='users/user.html', authentication_form=LoginForm), name='user'),
    path('exit', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
]