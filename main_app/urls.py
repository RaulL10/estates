from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.HouseList.as_view(), name='index'),
    path('houses/<int:house_id>/', views.houses_detail, name='detail'),
    path('houses/create/', views.HouseCreate.as_view(), name='houses_create'),
    path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='houses_update'),
    path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='houses_delete'),
    path('houses/<int:house_id>/add_listing/', views.add_listing, name='add_listing'),
    path('realtors/', views.RealtorList.as_view(), name='realtors_index'),
    path('realtors/<int:pk>/', views.RealtorDetail.as_view(), name='realtors_detail'),
    path('realtors/create/', views.RealtorCreate.as_view(), name='realtors_create'),
    path('realtors/<int:pk>/update/', views.RealtorUpdate.as_view(), name='realtors_update'),
    path('realtors/<int:pk>/delete/', views.RealtorDelete.as_view(), name='realtors_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('listings/', views.listings_index, name='listings_index'),
    path('houses/<int:house_id>/add_photo/', views.add_photo, name='add_photo')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)