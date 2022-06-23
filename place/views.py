from django.shortcuts import render
from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from place.serializers.place import PlaceListSerializer, PlaceSerializer
from .models import Place

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