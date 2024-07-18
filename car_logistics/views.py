from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Lot

def main(request):
    lots = Lot.objects.all()
    return render(request, 'car_logistics/main.html',
                  {
                      'lots': lots
                  })



def all_cars(request):
    lots = Lot.objects.all()[:20]  # Pagination logic can be added later
    return render(request, 'car_logistics/all_cars.html', {'lots': lots})

def new(request):
    lots = Lot.objects.filter(status='new')
    return render(request, 'car_logistics/new.html', {'lots': lots})

def dispatched(request):
    lots = Lot.objects.filter(status='dispatched')
    return render(request, 'car_logistics/dispatched.html', {'lots': lots})

def terminal(request):
    lots = Lot.objects.filter(status='terminal')
    return render(request, 'car_logistics/terminal.html', {'lots': lots})

def loading(request):
    lots = Lot.objects.filter(status='loading')
    return render(request, 'car_logistics/loading.html', {'lots': lots})

def shipped(request):
    lots = Lot.objects.filter(status='shipped')
    return render(request, 'car_logistics/shipped.html', {'lots': lots})

def unloaded(request):
    lots = Lot.objects.filter(status='unloaded')
    return render(request, 'car_logistics/unloaded.html', {'lots': lots})

def archived(request):
    lots = Lot.objects.filter(status='archived')
    return render(request, 'car_logistics/archived.html', {'lots': lots})


