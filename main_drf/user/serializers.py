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
class EmailFindSerializer(serializers.ModelSerializer):
    # Email
    class Meta:
        model = CustomUser
        fields = [
            'email'
        ]

class IdSerializer(serializers.ModelSerializer):
    # Email
    class Meta:
        model = CustomUser
        fields = [
            'username'
        ]