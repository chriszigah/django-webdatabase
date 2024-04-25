from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm, CreateRecordForm, UpdateRecordForm

# Create your views here.
from django.http import HttpResponse


from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from . models import Record

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
                return redirect('dashboard')
            
    context = {'form':form}

    return render(request, 'webdatabase/login.html', context=context)


# Users DashBoard
@login_required(login_url='login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webdatabase/dashboard.html', context=context)


# Create Record
@login_required(login_url='login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form':form}

    return render(request, 'webdatabase/create-record.html', context=context)

    
# Update Record
@login_required(login_url='login')
def update_record(request, id):
    record = Record.objects.get(id=id)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    
    context = {'form': form}

    return render(request, 'webdatabase/update-record.html', context=context)

# Read / View a singular record
@login_required(login_url='login')
def view_record(request, id):
    all_records = Record.objects.get(id=id)

    context = {'record': all_records}

    return render(request, 'webdatabase/view-record.html', context=context)


# Delete a record
@login_required(login_url='login')
def delete_record(request, id):
    record = Record.objects.get(id=id)
    record.delete()

    return redirect('dashboard')


# User Logout
def logout_user(request):
    auth.logout(request)
    return redirect("login")