from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def about(request):
    # return HttpResponse('Hello info page')
    return render(request, 'about.html')
