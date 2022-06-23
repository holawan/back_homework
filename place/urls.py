from django.urls import path 
from . import views 

app_name = 'place'

urlpatterns = [ 
    path('',views.place_list,name='place_list'),
    path('place/<int:place_pk>/',views.place_deatil,name='place_detail'),
]