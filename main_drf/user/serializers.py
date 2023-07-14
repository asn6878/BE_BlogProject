from rest_framework import serializers

from .models import CustomUser

# 기본 Base User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# User List Serializer
class UserListSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
            'date_joined'
        ]

# 이메일로 아이디 찾는 Serializer
class EmailFindSerializer(serializers.Serializer):
    # 모델 시리얼라이저 썼을때
    # class Meta:
    #     model = CustomUser
    #     fields = [
    #         'email'
    #     ]
    email = serializers.EmailField()
    

class IdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username'
        ]