from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Profile, EUser, Follow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EUser
        fields = ['username', 'avatar']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followers = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Profile
        fields = ['url', 'user', 'name', 'bio', 'cover', 'followers']
