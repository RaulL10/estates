from re import template
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import House, Realtor
from .forms import ListingForm, HouseSearchForm
import logging
from .models import Listing

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

class HouseIndexView(ListView):
    template_name = 'houses/index.html'
    context_object_name = 'houses'
    model = House

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['form'] = HouseSearchForm()
        return context

    def get_queryset(self):
        city = self.request.GET.get('city')
        zipcode = self.request.GET.get('zipcode')
        if zipcode and city:
            return House.objects.filter(city = city, zipcode=zipcode)
        elif city:
            return House.objects.filter(city = city)
        elif zipcode:
            return House.objects.filter(zipcode=zipcode)
        else:
            return House.objects.filter(user=self.request.user)

@login_required
def houses_detail(request, house_id):
  house = House.objects.get(id=house_id)
  try:
    listing = Listing.objects.filter(house_id=house_id).first()
  except:
    listing = None
  listing_form = ListingForm()
  return render(request, 'houses/detail.html', { 
    'house': house, 
    'listing_form': listing_form,
    'listing': listing,
  })

class HouseCreate(LoginRequiredMixin,CreateView):
  model = House
  fields = ['address', 'city', 'description', 'zipcode']
   # This inherited method is called when a
  # valid cat form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class HouseUpdate(LoginRequiredMixin, UpdateView):
  model = House
  fields = ['address', 'city', 'description' , 'zipcode']

class HouseDelete(LoginRequiredMixin ,DeleteView):
  model = House
  success_url = '/houses/'

def listings_index(request): 
  listings = Listing.objects.filter()
  return render(request, 'listings/index.html', { 'listings': listings })

@login_required
def add_listing(request, house_id):
  # create a ModelForm instance using the data in the posted form
  form = ListingForm(request.POST)
  # validate the data
  if form.is_valid():
    new_listing= form.save(commit=False)
    new_listing.house_id = house_id
    logging.warn(new_listing)
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
