from cmath import log
from django.forms import ModelForm, ModelChoiceField, ChoiceField
from .models import Listing, Realtor, House, CITIES
import logging

class RealtorChoiceField(ModelChoiceField):
  def label_from_instance(self, obj):
    logging.warn('i am here')
    return "Name: {}".format(obj.name)

class ListingForm(ModelForm):
  realtor = RealtorChoiceField(Realtor.objects)
  class Meta:
    model = Listing
    fields = ['realtor', 'price']

class HouseSearchForm(ModelForm):
  class Meta:
    model = House
    fields = ['city', 'zipcode']
  def __init__(self, *args, **kwargs):
    super(HouseSearchForm, self).__init__(*args, **kwargs)
    self.fields['zipcode'].required = False
    self.fields['city'] = ChoiceField(choices=[[None, '----------']] + [r for r in CITIES],required=False)
