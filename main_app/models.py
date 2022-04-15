from django.db import models
from django.urls import reverse

class Realtor(models.Model):
    name = models.CharField(max_length =200)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    def _str_(self):
        return self.name

class House(models.Model):
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    realtors = models.ManyToManyField(Realtor)
    def _str_(self):
        return self.address






# Create your models here.
