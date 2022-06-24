from django.shortcuts import render
from django.shortcuts import get_object_or_404,get_list_or_404
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import PointLog, User
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from place.serializers.place import PlaceListSerializer, PlaceSerializer
from place.serializers.review import ReviewImageSerializer, ReviewSerializer
from .models import Place, Review
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny]) 
def place_list(request):
    places = get_list_or_404(Place)
    # print(places)
    serializer = PlaceListSerializer(places, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def place_deatil(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)

    serializer = PlaceSerializer(place)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def review_list(request,place_pk) :
    reviews = Review.objects.filter(place_id=place_pk)
    serializer = ReviewSerializer(reviews,many=True)
    return Response(serializer.data)


class ReviewCreateView(APIView):

    permission_classes = (IsAuthenticated, )

    def post(self, request,place_pk):
        #작성된 리뷰 content와 사진필드가 둘다 없을 때, 예외처리
        if not request.data :
            return Response({'error' : '리뷰나 사진을 등록해주세요'}, status=status.HTTP_400_BAD_REQUEST)
        
        #필드는 존재하나 텍스트와 이미지가 둘 다 존재하지 않을 때 
        if not request.data['content'] and not request.data['image'] :
            return Response({'error' : '리뷰나 사진을 등록해주세요'}, status=status.HTTP_400_BAD_REQUEST)
       
       
        #작성된 리뷰 content나 사진이 있을 때, 
        point = 0
        serializer = ReviewSerializer(data=request.data, context={"request": request})
        
        place = get_object_or_404(Place, pk=place_pk)
        
        #첫 리뷰일 때 보너스 점수 
        if not (PlaceSerializer(place).data['reviews']) :
            point += 1 
        #유효성검사 통과하면 
        if serializer.is_valid():
            #저장 
            serializer.save(user=self.request.user,place=place)
            
            #사진이 있을 때             
            if serializer.data['images'] :
                point +=1 
            #내용이 있을 때 
            if serializer.data['content']  :
                print(serializer.data['content']) 
                point += 1 

            pointlog = PointLog.objects.create(user=self.request.user,place=place,
                        action='작성',calculation=True,point=point)
            pointlog.save()
            user = get_object_or_404(User,username=request.user)
            user.point += point 
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewUpdateView(APIView):

    permission_classes = (IsAuthenticated, )

    def put(self, request,place_pk,review_pk):
        #작성된 리뷰 content나 사진이 있을 때,
        review = get_object_or_404(Review,pk=review_pk) 
        point = 0
        serializer = ReviewSerializer(instance=review,data=request.data, context={"request": request,'review_pk':review_pk})
        
        place = get_object_or_404(Place, pk=place_pk)
        
        #첫 리뷰일 때 보너스 점수 
        if not (PlaceSerializer(place).data['reviews']) :
            point += 1 
        #유효성검사 통과하면 
        if serializer.is_valid():
            #저장 
            serializer.save(user=self.request.user,place=place)
            
            #사진이 있을 때             
            if serializer.data['images'] :
                point +=1 
            #내용이 있을 때 
            if serializer.data['content'] : 
                point += 1 

            pointlog = PointLog.objects.create(user=self.request.user,place=place,
                        action='작성',calculation=True,point=point)
            pointlog.save()

            user = get_object_or_404(User,username=request.user)
            user.point += point 
            user.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)