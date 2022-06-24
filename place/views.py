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
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

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

@api_view(['GET'])
def review_list(request,place_pk) :
    reviews = Review.objects.filter(place_id=place_pk)
    serializer = ReviewSerializer(reviews,many=True)
    return Response(serializer.data)


class ReviewCreateView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request,place_pk):
        serializer = ReviewSerializer(data=request.data, context={"request": request})
        place = get_object_or_404(Place, pk=place_pk)
        if serializer.is_valid():
            serializer.save(user=self.request.user,place=place)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)