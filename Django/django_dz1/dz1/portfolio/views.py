from django.shortcuts import render
from .models import Portfolio
# Create your views here.


def home(request):
    objects = Portfolio.objects.all()
    return render(request, 'portfolio/homepage.html', {'objects': objects})
