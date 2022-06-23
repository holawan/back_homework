from django.shortcuts import render
from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from place.serializers.place import PlaceListSerializer, PlaceSerializer
from place.serializers.review import ReviewImageSerializer, ReviewSerializer
from .models import Place, Review
from rest_framework.viewsets import ModelViewSet

# Create your views here.
@api_view(['GET'])
def place_list(request):
    places = get_list_or_404(Place)
    # print(places)
    serializer = PlaceListSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def place_deatil(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)

    serializer = PlaceSerializer(place)
    return Response(serializer.data)

@api_view(['GET','POST'])
def create_or_list_review(request, place_pk):
    def create_review() :
        user = request.user
        print(request.data)
        place = get_object_or_404(Place, pk=place_pk)
        serializer = ReviewSerializer(data=request.data,files=request.FILES)
        # print(serializer)
        lst = request.FILES.getlist('image')
        for _ in range(len(lst)) :
            print(lst[_])
            # image_serializer = ReviewImageSerializer(data=file)
            # if image_serializer.is_valid(raise_exception=True) : 
            #     image_serializer.save()
        if serializer.is_valid(raise_exception=True) :
            serializer.save(user=user,place=place)


            reviews = place.reviews.all()

            serializer = ReviewSerializer(reviews,many=True)
            
            return Response(serializer.data,status.HTTP_201_CREATED)

    def review_list() :
        reviews = Review.objects.filter(place_id=place_pk)
        serializer = ReviewSerializer(reviews,many=True)
        return Response(serializer.data)
    
    if request.method=='GET' : 
        return review_list()
    elif request.method == 'POST' :
        return create_review()

