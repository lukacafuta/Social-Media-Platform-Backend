from rest_framework import serializers

from friendRequest.models import FriendRequest
from userProfile.models import UserProfile


class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'


class FriendRequestUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = ['status']


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'avatar']
