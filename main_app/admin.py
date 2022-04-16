from django.contrib import admin

# Register your models here.
from .models import House, Realtor, Listing




# Register your models here

admin.site.register(House)
admin.site.register(Listing)
admin.site.register(Realtor)