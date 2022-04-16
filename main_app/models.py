from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

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
      return reverse('detail', kwargs={'pk': self.id})

class House(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    realtors = models.ManyToManyField(Realtor)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
     return self.name
     
    def get_absolute_url(self):
     return reverse('detail', kwargs={'house_id': self.id})
   
  

class Meta:
  ordering = ['-date']


class Listing(models.Model):
  date = models.DateField('Listing Date')
  location = models.CharField(max_length=200,
    # add the 'choices' field option
    choices=CITIES,
    # set the default to be 'B'
    default=CITIES[0][0]
  )
  # creates a cat_id column
  house = models.ForeignKey(
    House,
    # automatically delete all feedings with the cat
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_location_display()} on {self.date}"





# Create your models here.
