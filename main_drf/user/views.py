from django.shortcuts import render

# drf 관련 모듈
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# 모델 및 시리얼라이저 관련 모듈
from .serializers import UserSerializer, UserListSerializer
from .models import CustomUser as User

# swagger Request Params 관련 모듈
from drf_yasg.utils import swagger_auto_schema
from .swaggers import CustomUserBodySerializer

class UserView(APIView):
    permission_classes = [AllowAny]

    # user 리스트 조회
    def get(self, request):
        user_data_list = User.objects.all()
        serializer = UserListSerializer(user_data_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # user 생성
    @swagger_auto_schema(request_body=CustomUserBodySerializer)
    def post(self, request):
        user_serializer = UserSerializer(data = request.data)

        if (user_serializer.is_valid()):
            saved_user = user_serializer.save()
            # print("saved_user =",saved_user)
            return Response(
                {
                    'your user' : user_serializer.data,
                },
                status=status.HTTP_201_CREATED
            )      
        return Response(
            {
                'errors':user_serializer.errors,
                'message' : "인풋 값 확인 요망",
            }, status = status.HTTP_400_BAD_REQUEST
        )
    

# id 를 사용한 user 조회
class UserDetailView(APIView):
    def get(self, request, pk):
        user_data = User.objects.get(id = pk)
        user_serializer = UserSerializer(user_data)

        return Response(user_serializer.data, status= status.HTTP_200_OK)
    
    # user 수정
    def put(self, request, pk):
        user_data = User.objects.get(id = pk)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # user 삭제
    def delete(self, request, pk):
        print(request)
        print(dir(request))
        user_data = User.objects.get(id = pk)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
