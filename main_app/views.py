from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import House, Realtor
from .forms import CustomMultiSelectForm, ListingForm
import logging
from .models import Listing
# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def houses_index(request):
   houses = House.objects.filter(user=request.user)
   return render(request, 'houses/index.html', { 'houses': houses })

@login_required
def houses_detail(request, house_id):
  house = House.objects.get(id=house_id)
  # listing_form = ListingForm()
  # id_list = house.realtors.all().values_list('id')
  listing_form = ListingForm()
  return render(request, 'houses/detail.html', { 
    'house': house, 
    'listing_form': listing_form,
  })

class HouseCreate(LoginRequiredMixin,CreateView):
  model = House
  form_class = CustomMultiSelectForm
  # fields = ['address', 'city', 'description' , 'price' , 'zipcode']
   # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class HouseUpdate(LoginRequiredMixin, UpdateView):
  model = House
  fields = ['address', 'city', 'realtor', 'description' , 'price' , 'zipcode']

class HouseDelete(LoginRequiredMixin ,DeleteView):
  model = House
  success_url = '/houses/'

@login_required
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
  fields = ['name' , 'description' ,'phone' , 'email']

class RealtorDelete(DeleteView):
  model = Realtor
  success_url = '/realtors/'

@login_required
def assoc_realtor(request, house_id, realtor_id):
  House.objects.get(id=house_id).realtors.add(realtor_id)
  return redirect('detail', house_id=house_id)

@login_required
def unassoc_realtor(request, house_id, realtor_id):
  House.objects.get(id=house_id).realtors.remove(realtor_id)
  return redirect('detail', house_id=house_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
