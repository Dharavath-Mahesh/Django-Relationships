from django.shortcuts import render
from .models import *

# Create your views here.
def onetoone(request):
    vehicle2 = Vehicle.objects.all()
    car = Car.objects.all()

    context = {
        'vehicle2': vehicle2,
        'car': car,
    }
    return render(request, 'one-to-one.html', context)