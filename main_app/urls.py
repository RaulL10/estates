from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='houses_index'),
]