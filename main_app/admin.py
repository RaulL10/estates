from django.contrib import admin

# from main_app.models import images

# Register your models here.
from .models import House, Realtor, Listing, Photo
from django.contrib import admin
# from .models import images


class AdminImages(admin.ModelAdmin):    
    list_display = ['id_no','name','loc','image','profile']

# Register your models here

admin.site.register(House)
admin.site.register(Listing)
admin.site.register(Realtor)
admin.site.register(Photo)
# admin.site.register(images, AdminImages)