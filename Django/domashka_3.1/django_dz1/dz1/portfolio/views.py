from django.shortcuts import render, redirect
from .models import Portfolio, Info
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError


# Create your views here.


def home(request):
    objects = Portfolio.objects.all()
    return render(request, 'portfolio/homepage.html', {'objects': objects})


def autor(request):
    return render(request, 'portfolio/autor.html')


def info(request):
    cards = Info.objects.all()
    return render(request, 'portfolio/info.html', {'cards': cards})


def signup_user(request):
    if request.method == 'GET':
        return render(request, 'portfolio/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'portfolio/signupuser.html',
                              {'form': UserCreationForm(),
                               'error': 'Пользователь с таким именем уже существует, выберите другое имя'})
        else:
            return render(request, 'portfolio/signupuser.html',
                          {'form': UserCreationForm(), 'error': 'Введенные пароли не совпадают'})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def login_user(request):
    if request.method == 'GET':
        return render(request, 'portfolio/loginuser.html',
                      {'form': AuthenticationForm()})

    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'portfolio/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Неверное имя пользователя или пароль'})
        else:
            login(request, user)
            return redirect('home')