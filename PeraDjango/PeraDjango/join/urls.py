from django.contrib import admin
from django.urls import path, include
from .views import join, userLogin, userSuccessLogin, userLogout

urlpatterns = [
    path('join/', join(), name='join'),
    path('login/', userLogin(), name='userLogin'),
    path('user/', userSuccessLogin(), name='userSuccessLogin'),
    path('logout/', userLogout(), name='userLogout'),
]
