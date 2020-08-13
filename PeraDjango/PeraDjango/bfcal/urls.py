from django.contrib import admin
from django.urls import path, include
from .views import bfcal
from .views import bfcalResults

urlpatterns = [
    path('bfcal/', bfcal(), name='bfcal'),
    path('results/', bfcalResults(), name='bfcalResult'),
]
