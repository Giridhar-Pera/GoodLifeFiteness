from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import CrateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def join(request):
    # return HttpResponse('Hello info page')
    form = CrateUserForm()

    if request.method == 'POST':
        form = CrateUserForm(request.POST)
        requestData = request.POST
        if form.is_valid():
            form.save()
            user = requestData.get('username')
            messages.success(request, 'Successfully user created for ' + user)
            return render(request, 'login.html', {})

    context = {'form': form}
    return render(request, 'register.html', context)


def userLogin(request):
    if request.method == 'POST':
        requestData = request.POST
        user = requestData.get('username')
        password = requestData.get('password')

        loggedUser = authenticate(request, username=user, password=password)

        if loggedUser is not None:
            login(request, loggedUser)
            return redirect('/blog')
        else:
            messages.info(request, 'Login failed')

    return render(request, 'login.html')


@login_required(login_url='/login')
def userSuccessLogin(request):
    user = request.user

    context = {'username': user}

    return render(request, 'user_success_login.html', context)


@login_required(login_url='/login')
def userLogout(request):
    logout(request)
    return redirect('/login')
