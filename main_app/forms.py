from cmath import log
from django.forms import ModelForm, CharField, Textarea, IntegerField, MultipleChoiceField, SelectMultiple
from .models import House, Listing, Realtor
import logging


class ListingForm(ModelForm):
  class Meta:
    model = Listing
    fields = ['date', 'location']

class CustomMultiSelectForm(ModelForm):
  address = CharField()
  city = CharField()
  zipcode = CharField()
  description = Textarea()
  price = IntegerField()
  choices_query = Realtor.objects.all()
  choices = []
  for e in choices_query:
    choices.append((e.id, e.name))
  # logging.warn(choices)
  realtors = MultipleChoiceField(
      choices=choices,
      widget=SelectMultiple
  )

  def __init__(self, *args, **kwargs):
      super(CustomMultiSelectForm, self).__init__(*args, **kwargs)
      choices_query = Realtor.objects.all()
      choices = []
      for e in choices_query:
        choices.append((e.id, e.name))
      self.fields['realtors'].choices = choices


  class Meta:
    model = House
    fields = ['address', 'city', 'description' , 'price' , 'zipcode', 'realtors']