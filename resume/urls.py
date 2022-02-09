from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume, name='resume'),
    path('emp/', views.resume_all_employment, name='resume_emp'),
    path('edu/', views.resume_all_education, name='resume_edu'),
]