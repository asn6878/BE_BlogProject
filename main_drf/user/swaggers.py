from rest_framework import serializers

class CustomUserBodySerializer(serializers.Serializer):
    username = serializers.CharField(help_text="username")
    password = serializers.CharField(help_text="password")
    nickname = serializers.CharField(help_text="nickname")