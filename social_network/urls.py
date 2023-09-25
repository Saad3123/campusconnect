# social_network/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.signup, name='signup'),
    path("index/", views.index, name='index'),
    path("login/", views.login_view, name='login'),
    path("signup", views.signup, name="signup"),
]
