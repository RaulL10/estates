from django.shortcuts import render
from .models import House, Realtor

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def houses_index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', { 'houses': houses })

