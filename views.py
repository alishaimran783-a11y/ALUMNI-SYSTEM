from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import AlumniRegistrationForm
from .models import Alumni

def home(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    if request.method == 'POST':
        form = AlumniRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('directory')
    else:
        form = AlumniRegistrationForm()
    return render(request, 'register.html', {'form': form})

def directory(request):
    alumnis = Alumni.objects.all()
    return render(request, 'directory.html', {'alumnis': alumnis})