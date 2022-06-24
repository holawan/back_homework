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
    content = models.TextField(null=True,blank=True)

    def __str__(self):
        if self.content :

            return f'{self.pk}번째 리뷰 : {self.content}'
        else :
            return f'{self.pk}번째 리뷰 : 내용 없음'

#이미지를 여러개 추가하기 위해 1:N관계 형성 
class ReviewImage(models.Model) :
    #이미지를 넣을 리뷰 참조 
    review = models.ForeignKey(Review,on_delete=models.CASCADE)
    #이미지 
    image = models.ImageField(upload_to='review/',blank=True, null=True)
