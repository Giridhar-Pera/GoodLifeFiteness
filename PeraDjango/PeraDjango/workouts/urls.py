from django.contrib import admin
from django.urls import path, include
from .views import workouts

urlpatterns = [
    path('workouts/', workouts(), name='workouts'),
]
