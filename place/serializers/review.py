from django.shortcuts import get_object_or_404
from rest_framework import serializers
from place.models import Review, ReviewImage

from rest_framework import serializers
from place.models import Review, ReviewImage
class ReviewImageSerializer(serializers.ModelSerializer):
   class Meta:
      model = ReviewImage
      fields = ['id']


class ReviewSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    def get_images(self, obj):
        image = obj.reviewimage_set.all()
        return ReviewImageSerializer(instance=image, many=True).data
    class Meta:
        model = Review
        fields = ('id', 'content','images', 'user', 'place')
        read_only_fields = ('user','place')


    def create(self, validated_data):
        images_data = self.context['request'].FILES
        review = Review.objects.create(**validated_data)
        for image_data in images_data.getlist('image'):
            ReviewImage.objects.create(review=review, image=image_data)
        return review
    
    def update(self, instance,validated_data):
        images_data = self.context['request'].FILES
        instance.content = validated_data.get('content',instance.content)
        review = get_object_or_404(Review,pk=self.context['review_pk'])
        review.content = validated_data.get('content',instance.content)
        review.save()
        
        raw_data = review.reviewimage_set.all() 
        new_data = images_data.getlist('image')

        raw_data_length = len(raw_data)
        new_data_length = len(new_data)
        #길이가 같을 때 
        if raw_data_length == new_data_length :
            for i in range(raw_data_length) :
                tmp_image = get_object_or_404(ReviewImage,pk = raw_data[i].pk)
                if str(tmp_image.image)[7:] == str(new_data[i]) :
                    continue
                tmp_image.image = new_data[i]
                tmp_image.save()
        #원래 데이터가 더 많을 때, 
        elif raw_data_length > new_data_length :
            for i in range(new_data_length) :
                tmp_image = get_object_or_404(ReviewImage,pk = raw_data[i].pk)
                if str(tmp_image.image)[7:] == str(new_data[i]) :
                    continue
                tmp_image.image = new_data[i]
                tmp_image.save()
            for i in range(new_data_length,raw_data_length) :
                tmp_image = get_object_or_404(ReviewImage,pk = raw_data[i].pk)
                tmp_image.delete()
        #새로 들어온 데이터가 더 많을 때
        elif raw_data_length < new_data_length :
            for i in range(raw_data_length) :
                tmp_image = get_object_or_404(ReviewImage,pk = raw_data[i].pk)
                if str(tmp_image.image)[7:] == str(new_data[i]) :
                    continue
                tmp_image.image = new_data[i]
                tmp_image.save()
            for i in range(raw_data_length,new_data_length) :
                ReviewImage.objects.create(review=review, image=new_data[i])
        return review
