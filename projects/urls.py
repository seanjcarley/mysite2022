import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('simon/', views.simon, name='simon'),
    path('mastermind/', views.mastermind, name='mastermind'),
]
