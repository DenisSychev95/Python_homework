from django.shortcuts import render
from .models import Portfolio, Info


# Create your views here.


def home(request):
    objects = Portfolio.objects.all()
    return render(request, 'portfolio/homepage.html', {'objects': objects})


def autor(request):
    return render(request, 'portfolio/autor.html')


def info(request):
    cards = Info.objects.all()
    return render(request, 'portfolio/info.html', {'cards': cards})
