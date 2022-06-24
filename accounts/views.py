from django.shortcuts import get_list_or_404, render
from django.shortcuts import get_object_or_404 
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view 
from rest_framework.response import Response

from accounts.models import PointLog

from .serializers import SignupSerializer, UserPointSerializer, UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
# Create your views here.

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny]) 
def signup(request) :
    if User.objects.filter(username=request.data.get('username')).exists() :
        return Response({'error' : '일치하는 아이디가 존재합니다.'},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST' :
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response({'message':'ok','id':request.data['username']},status=status.HTTP_201_CREATED)
        else :
            return Response({"message" : "Request Body Error"},status=status.HTTP_409_CONFLICT)

@api_view(['GET'])
def pointlog(request,user_pk):
    userlog = get_list_or_404(PointLog,user=user_pk)
    serializer = UserPointSerializer(userlog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def point(request,user_pk):
    user = get_object_or_404(User,pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)