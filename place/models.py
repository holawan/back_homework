from django.db import models
from django.conf import settings
# Create your models here.

class Place(models.Model) :
    place_name = models.CharField(max_length=20)
    place_tagline = models.TextField()

    def __str__(self):
        return self.place_name

class Review(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reviews')
    place = models.ForeignKey(Place,on_delete=models.CASCADE,related_name='reviews')
    content = models.TextField()

    def __str__(self):
        return self.content

class ReviewImage(models.Model) :
    review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='image')
    image = models.ImageField(upload_to='thumbnails/review/',blank=True, null=True)
    
class Point(models.Model) :
    review = models.ForeignKey(Review,on_delete=models.CASCADE,related_name='point')
    action = models.CharField(max_length=10)
    calculation = models.BooleanField()
    point = models.IntegerField()
    point_now = models.IntegerField()

