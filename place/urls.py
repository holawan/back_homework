from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter

app_name = 'place'

urlpatterns = [ 
    path('',views.place_list,name='place_list'),
    path('place/<int:place_pk>/',views.place_deatil,name='place_detail'),
    # path('place/<int:place_pk>/reviews/', views.review_list),
    path('place/<int:place_pk>/reviews/',views.ReviewListCreateView.as_view()),
    path('place/<int:place_pk>/review_update/<int:review_pk>/',views.ReviewUpdateOrDeleteView.as_view()),
]