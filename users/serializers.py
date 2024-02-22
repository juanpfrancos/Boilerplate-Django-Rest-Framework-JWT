from rest_framework import serializers
from drf_spectacular.utils import extend_schema
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    @extend_schema(request=CustomUser)
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
