from django.test import TestCase
from django.test import Client
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status


c = Client() 
login_url = reverse('accounts:gettoken')
response = c.post(login_url,{'username':'admin','password':'dlatl12!@'})
print(response.content)