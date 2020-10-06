from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Profile


class LoginSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(max_length=30, required=True)
    last_name = serializers.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate_password(self, value):
        return make_password(value)

    def create(self, validated_data):
        validated_data['is_active'] = True
        groups = validated_data.pop('groups')
        user_permissions = validated_data.pop('user_permissions')
        user = User(**validated_data)
        user.save()
        if groups:
            user.groups.set(groups)
        if user_permissions:
            user.user_permissions.set(user_permissions)
        return user


class UserUpdateSerializer(ModelSerializer):
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name']
