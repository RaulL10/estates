from django.shortcuts import render, redirect
import logging

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import House, Realtor
from .forms import ListingForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def houses_index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', { 'houses': houses })

def houses_index(request, finch_id):
  house = House.objects.get(id=finch_id)
  listing_form = ListingForm()
  id_list = house.realtors.all().values_list('id')
  realtors_house_doesnt_have = Realtor.objects.exclude(id__in=id_list)
  logging.warning(realtors_house_doesnt_have)
  return render(request, 'houses/detail.html', { 'house': house, 
  'listing': listing_form,
  'studys': realtors_house_doesnt_have
  })

class HouseCreate(CreateView):
  model = House
  fields = ['name', 'type', 'description', 'age']

class HouseUpdate(UpdateView):
  model = House
  fields = ['type', 'description', 'age']

class HouseDelete(DeleteView):
  model = House
  success_url = '/houses/'

def add_listing(request, house_id):
  # create a ModelForm instance using the data in the posted form
  form = ListingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_listing= form.save(commit=False)
    new_listing.house_id = house_id
    new_listing.save()
  return redirect('detail', house_id=house_id)

class RealtorList(ListView):
  model = Realtor

class RealtorDetail(DetailView):
  model = Realtor

class RealtorCreate(CreateView):
  model = Realtor
  fields = '__all__'

class RealtorUpdate(UpdateView):
  model = Realtor
  fields = ['topic']

class RealtorDelete(DeleteView):
  model = Realtor
  success_url = '/studys/'

def assoc_realtor(request, house_id, realtor_id):
  House.objects.get(id=house_id).realtors.add(realtor_id)
  return redirect('detail', house_id=house_id)

def unassoc_realtor(request, house_id, realtor_id):
  House.objects.get(id=house_id).realtors.remove(realtor_id)
  return redirect('detail', house_id=house_id)

