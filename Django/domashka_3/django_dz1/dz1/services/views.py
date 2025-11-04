from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Services


def services(request):
    elements = Services.objects.all()
    return render(request, 'services/services.html', {'elements': elements})


def detail(request, detail_id):
    elem = get_object_or_404(Services, pk=detail_id)
    return render(request, 'services/detail.html', {'elem': elem})
