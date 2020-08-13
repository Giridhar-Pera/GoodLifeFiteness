from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def workouts(request):
    # return HttpResponse('Hello info page')
    return render(request, 'workouts.html')
