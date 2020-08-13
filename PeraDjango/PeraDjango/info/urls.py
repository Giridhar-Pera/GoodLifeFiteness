from django.contrib import admin
from django.urls import path, include
from .views import info

urlpatterns = [
    path('', info(), name='info'),
]
