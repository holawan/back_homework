from django.db import models
from django.contrib.auth.models import AbstractUser

from place.models import Place
# Create your models here.


class User(AbstractUser) :
    point = models.IntegerField(default=0)
# class Point(models.Model) :
#     #유저의 현재 포인트 
#     point_now = models.OneToOneField(User,on_delete=models.CASCADE,related_name='point',default=0)

class PointLog(models.Model) :
    #리뷰를 지워도 로그는 보관하도록 SET_DEFALUT 설정 
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='pointLog')
    #리뷰를 작성한 장소 
    place = models.ForeignKey(Place,on_delete=models.CASCADE)
    #생성,수정,삭제인지 action 확인 
    action = models.CharField(max_length=10)
    #증/감여부 
    calculation = models.BooleanField()
    #부여하거나 차감할 포인트
    point = models.IntegerField()
