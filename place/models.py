from django.db import models
from django.conf import settings
# Create your models here.

class Place(models.Model) :
    #장소명 
    place_name = models.CharField(max_length=20)
    #장소 소개 
    place_tagline = models.TextField()

    def __str__(self):
        return self.place_name

class Review(models.Model) :
    #글쓴 유저 참조 
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reviews')
    #리뷰를 쓰는 장소 참조 
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='reviews')
    #리뷰 내용 
    content = models.TextField()

    def __str__(self):
        return self.content

#이미지를 여러개 추가하기 위해 1:N관계 형성 
class ReviewImage(models.Model) :
    #이미지를 넣을 리뷰 참조 
    review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='image')
    #이미지 
    image = models.ImageField(upload_to='thumbnails/review/',blank=True, null=True)
    
class Point(models.Model) :
    #리뷰를 지워도 로그는 보관하도록 SET_DEFALUT 설정 
    review = models.ForeignKey(Review,on_delete=models.SET_DEFAULT,default = 'deleted_review',related_name='point')
    #생성,수정,삭제인지 action 확인 
    action = models.CharField(max_length=10)
    #증/감여부 
    calculation = models.BooleanField()
    #부여하거나 차감할 포인트
    point = models.IntegerField()
    #유저의 현재 포인트 
    point_now = models.IntegerField()

