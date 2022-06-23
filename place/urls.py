from django.urls import path 
from . import views 
from rest_framework.routers import DefaultRouter

app_name = 'place'

urlpatterns = [ 
    path('',views.place_list,name='place_list'),
    path('place/<int:place_pk>/',views.place_deatil,name='place_detail'),
    path('place/<int:place_pk>/reviews/', views.create_or_list_review),
]