from django.contrib import admin

# Register your models here.
from .models import House, Realtor, Listing
from django.contrib import admin


admin.site.register(House)
admin.site.register(Listing)
admin.site.register(Realtor)