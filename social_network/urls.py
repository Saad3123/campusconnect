# social_network/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # Add more URLs as needed
]