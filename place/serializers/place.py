from rest_framework import serializers

from place.models import Place, Review


class PlaceListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Place
        fields = ('pk','place_name')



class PlaceSerializer(serializers.ModelSerializer):
    
    class ReviewSerializer(serializers.ModelSerializer) :
        class Meta :
            model = Review
            fields = ('content',)
    
    reviews = ReviewSerializer(read_only=True,many=True)
    class Meta:
        model = Place
        fields = ('place_name','place_tagline','reviews',)
