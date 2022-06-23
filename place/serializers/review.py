from rest_framework import serializers
from accounts.serializers import UserSerializer

from place.models import Review, ReviewImage
from place.serializers.place import PlaceListSerializer, PlaceSerializer


class ReviewImageSerializer(serializers.ModelSerializer):

    image = serializers.ImageField()

    class Meta:
        model = ReviewImage
        fields = ('image',)

class ReviewSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    # place = PlaceListSerializer(read_only=True)
    # images = ReviewImageSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ('pk', 'user', 'place', 'content',)
        read_only_fields = ('user','place')

    # def create(self,validated_data) :
    #     for image in self :
    #         print(image)
    #     print('context:', self.context)
    #     print(validated_data)
    #     return 
    def create(self, validated_data,files):
        print(self)
        # print(files)
        images_data = self
        review = Review.objects.create(**validated_data)
        for image_data in images_data.getlist('image'):
            ReviewImage.objects.create(review=review, image=image_data)
        return review