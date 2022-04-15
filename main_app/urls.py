from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='houses_index'),
#     path('houses/<int:house_id>/', views.houses_detail, name='detail'),
#     path('houses/create/', views.HouseCreate.as_view(), name='houses_create'),
#     path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='houses_update'),
#     path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='houses_delete'),
#     path('houses/<int:house_id>/add_feeding/', views.add_feeding, name='add_feeding'),
#     path('houses/<int:house_id>/assoc_study/<int:study_id>/', views.assoc_study, name='assoc_study'),
#     path('houses/<int:house_id>/unassoc_study/<int:study_id>/', views.unassoc_study, name='unassoc_study'),
#     path('studys/', views.StudyList.as_view(), name='studys_index'),
#     path('stuyds/<int:pk>/', views.StudyDetail.as_view(), name='studys_detail'),
#     path('studys/create/', views.StudyCreate.as_view(), name='studys_create'),
#     path('studys/<int:pk>/update/', views.StudyUpdate.as_view(), name='studys_update'),
#     path('studys/<int:pk>/delete/', views.StudyDelete.as_view(), name='studys_delete'),
# ]
    
]