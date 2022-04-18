import logging
from numbers import Real
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

CITIES = (
  ('S', 'San Diego'),
  ('B', 'Santa Barabara'),
  ('M', 'Malibu')
)

class Realtor(models.Model):
    name = models.CharField(max_length =200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def _str_(self):
      return self.name

    def get_absolute_url(self):
      return reverse('realtors_detail', kwargs={'pk': self.id})



class House(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200,
      choices=CITIES,
      default=CITIES[0][0]
    )
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
     return f"{self.get_city_display()}"
     
    def get_absolute_url(self):
     return reverse('detail', kwargs={'house_id': self.id})



class Listing(models.Model):
  class Meta:
    ordering = ['-date']

  date = models.DateField(auto_now=True)
  realtor = models.ForeignKey(
    Realtor,
    on_delete=models.CASCADE,
    default=1
  )
  house = models.ForeignKey(
    House,
    on_delete=models.CASCADE
  )
  price = models.IntegerField(default=100000)

  def __str__(self):
    return f"{self.house.address + ' ' + self.house.city}"

