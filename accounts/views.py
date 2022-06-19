from django.shortcuts import render
from django.shortcuts import get_object_or_404 
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from .serializers import SignupSerializer


# Create your views here.

User = get_user_model()

@api_view(['POST'])
def signup(request) :
    if request.method == 'POST' :
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response({'message':'ok'},status=status.HTTP_201_CREATED)
        else :
            return Response({"message" : "Request Body Error"},status=status.HTTP_409_CONFLICT)
