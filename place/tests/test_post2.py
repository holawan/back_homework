from django.test import TestCase

# Create your tests here.
from django.shortcuts import get_object_or_404
from django.test import Client
from django.urls import reverse
import json
import requests
from place.models import Place
from django.contrib.auth import get_user_model
c = Client() 




User = get_user_model()
# test라는 유저가 존재하는지 확인 
is_user = User.objects.filter(username='test2').exists()
#존재하지 않는다면 회원가입 
if not is_user :
    signup_url = reverse('accounts:signup')

    response = c.post(signup_url,{'username':'test2','password':'test12!@'})

#로그인 
login_url = reverse('accounts:gettoken')
#토큰 발급 
response = c.post(login_url,{'username':'test2','password':'test12!@'})

#토큰 가져오기 
jwt =  json.loads(response.content)['token']
#포인트 조회 테스트 
place = get_object_or_404(Place,place_name='한강')

#유저의 포인트 로그 조회 
create_review_url = f"http://127.0.0.1:8000/api/v1/places/place/{place.pk}/reviews/"
token = f'JWT {jwt}'

#토큰 실어주기 
headers = {
  'Authorization': token,
}
import os 
pathname = os.getcwd()

payload={"content" : "저는 테스트2번입니다. 한강 너무 좋았어요"}
files=[
  # ('image',('boj.png',open(f'{pathname}/test_image/한강.jpg','rb'),'image/png'))
]
#응답 결과 출력 
response = requests.request("POST", create_review_url, headers=headers,data=payload, files=files)

print(response.text)
