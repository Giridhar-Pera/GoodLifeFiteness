"""PeraDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .info.views import info
from .about.views import about
from .bfcal.views import bfcal
from .join.views import join, userLogin, userSuccessLogin, userLogout
from .bfcal.views import bfcalResults
from .workouts.views import workouts
from .blog.views import blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', info),
    path('about/', about),
    path('bfcal/', bfcal),
    path('join/', join),
    path('results/', bfcalResults),
    path('workouts/', workouts),
    path('login/', userLogin),
    path('user/', userSuccessLogin),
    path('logout/', userLogout),
    path('blog/', include('PeraDjango.blog.urls'))
]
