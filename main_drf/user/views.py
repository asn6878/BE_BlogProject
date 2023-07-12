from django.shortcuts import render

# drf 관련 모듈
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

# 모델 및 시리얼라이저 관련 모듈
from .serializers import UserSerializer, UserListSerializer, EmailFindSerializer, IdSerializer
from .models import CustomUser as User

# swagger Request Params 관련 모듈
from drf_yasg.utils import swagger_auto_schema
from .swaggers import CustomUserBodySerializer

class UserView(APIView):
    # user 리스트 조회
    def get(self, request):
        permission_classes = [IsAuthenticated]
        user_data_list = User.objects.all()
        serializer = UserListSerializer(user_data_list, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # user 생성
    @swagger_auto_schema(request_body=CustomUserBodySerializer)
    def post(self, request):
        permission_classes = [IsAuthenticated]
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
                'errors': user_serializer.errors,
                'message' : "인풋 값 확인 요망",
            }, status = status.HTTP_400_BAD_REQUEST
        )
    

# id 를 사용한 user 조회
class UserDetailView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, pk):
        user_data = User.objects.get(id = pk)
        user_serializer = UserSerializer(user_data)

        return Response(user_serializer.data, status= status.HTTP_200_OK)
    
# id 를 사용한 user 수정 및 삭제
class UserDetailManagementView(APIView):
    permission_classes = [IsAuthenticated]

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
        user_data = User.objects.get(id = pk)
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 이메일로 아이디 찾기
class EmailFindView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailFindSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email = serializer.data['email']).exists():
                user_id = User.objects.get(email = serializer.data['email']).username
                response_data = JsonResponse(user_id)
                return Response(response_data, status=status.HTTP_200_OK)
            else :
                response_data = JsonResponse({
                        "message" : "해당 이메일로 가입된 아이디가 없습니다."
                    })
                return Response(response_data, status=status.HTTP_400_BAD_REQUEST
                )