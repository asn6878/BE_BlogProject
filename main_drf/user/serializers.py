from rest_framework import serializers

from .models import CustomUser

# 기본 Base User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

#
class UserListSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = CustomUser
        fields = [
            'id',
            'username',
            'nickname'
        ]
