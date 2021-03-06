from rest_framework import serializers

from place.models import Place, Review


class PlaceListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = ('pk','place_name')


class DummyReviewSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Review
        fields = ('user','content',)

class PlaceSerializer(serializers.ModelSerializer):
    
    
    reviews = DummyReviewSerializer(read_only=True,many=True)
    class Meta:
        model = Place
        fields = ('pk','place_name','place_tagline','reviews',)
        
