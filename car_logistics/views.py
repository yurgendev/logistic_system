from django.shortcuts import render
from django.http import HttpResponse
from .models import Lot

def main(request):
    lots = Lot.objects.all()
    return render(request, 'main.html',
                  {
                      'lots': lots
                  })