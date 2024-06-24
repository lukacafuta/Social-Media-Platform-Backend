from rest_framework import serializers
from userProfile.models import UserProfile


class FollowerUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username']