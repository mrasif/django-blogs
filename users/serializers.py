from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password',)

    def create(self, validated_data):
        user=get_user_model().objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(style={'input_type':'email'}, required=True)
    password = serializers.CharField(style={'input_type':'password'})
    
    class Meta:
        fields = ('email','password',)