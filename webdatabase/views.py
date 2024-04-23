from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm

# Create your views here.
from django.http import HttpResponse


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'webdatabase/index.html')


# - Register
def register(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}

    return render(request, 'webdatabase/register.html', context=context)


# Login a user
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                #return redirect('')
    context = {'form':form}

    return render(request, 'webdatabase/login.html', context=context)


# Users DashBoard
@login_required(login_url='login')
def dashbaord(request):
    return render(request, 'webdatabase/dashboard.html')






# User Logout
def logout_user(request):
    auth.logout(request)
    return redirect("login_user")