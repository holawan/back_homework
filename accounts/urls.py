from django.urls import path 
from . import views 

app_name = 'accounts'

from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [ 
    path('signup/',views.signup,name='signup'),
    path('gettoken/',obtain_jwt_token)
]