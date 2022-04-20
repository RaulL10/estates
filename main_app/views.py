
   
from re import template
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import House, Realtor, Photo
from .forms import ListingForm, HouseSearchForm
import logging
from .models import Listing
import boto3
import os
import uuid


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


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

@login_required
def listings_index(request): 
  listings = Listing.objects.filter()
  return render(request, 'listings/index.html', { 'listings': listings })


@login_required
def add_listing(request, house_id):
  form = ListingForm(request.POST)
  if form.is_valid():
    new_listing= form.save(commit=False)
    new_listing.house_id = house_id
    logging.warn(new_listing)
    new_listing.save()
  return redirect('detail', house_id=house_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)



def add_photo(request, house_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, house_id=house_id)
        except Exception as e:
            print('An error occured uploading file to S3')
            print(e)
  return redirect('detail', house_id=house_id)


# CLASS BASED VIEWS
class HouseList(LoginRequiredMixin, ListView):
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
            return House.objects.all()




class HouseCreate(LoginRequiredMixin, CreateView):
  model = House
  fields = ['address', 'city', 'description', 'zipcode']

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)



class HouseUpdate(LoginRequiredMixin, UpdateView):
  model = House
  fields = ['address', 'city', 'description' , 'zipcode']



class HouseDelete(LoginRequiredMixin ,DeleteView):
  model = House
  success_url = '/houses/'





class RealtorList(LoginRequiredMixin ,ListView):
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
