from django.shortcuts import get_object_or_404
from django.test import Client
from django.urls import reverse
import json
import requests
from django.contrib.auth import get_user_model

c = Client() 



User = get_user_model()
# test라는 유저가 존재하는지 확인 
is_user = User.objects.filter(username='test').exists()
#존재하지 않는다면 회원가입 
if not is_user :
    signup_url = reverse('accounts:signup')

    response = c.post(signup_url,{'username':'test','password':'test12!@'})

#로그인 
login_url = reverse('accounts:gettoken')
#토큰 발급 
response = c.post(login_url,{'username':'test','password':'test12!@'})

#토큰 가져오기 
jwt =  json.loads(response.content)['token']
#포인트 조회 테스트 
user = get_object_or_404(User,username='test')

#유저의 포인트 로그 조회 
pointlog_url = f'http://127.0.0.1:8000/api/v1/accounts/pointlog/{user.pk}/'
token = f'JWT {jwt}'

#토큰 실어주기 
headers = {
  'Authorization': token,
}

#응답 결과 출력 
response = requests.request("GET", pointlog_url, headers=headers)

print(f'{user.username}의 포인트 로그{response.text}')


point_url = f'http://127.0.0.1:8000/api/v1/accounts/point/{user.pk}/'

response = requests.request("GET", point_url, headers=headers)
print(f'{user.username}의 현재 point{response.text}')