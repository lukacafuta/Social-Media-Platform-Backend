from django.shortcuts import render
from rest_framework import status, mixins
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from follower.models import Follower
from follower.serializers import UserProfileSerializer
from userProfile.models import UserProfile


# Create your views here.
class ListFollowersView(GenericAPIView, mixins.ListModelMixin):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user_profile = self.request.user.userprofile
        followers = Follower.objects.filter(isFollowed=current_user_profile)
        return [follower.isFollowing for follower in followers]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListFollowingView(GenericAPIView, mixins.ListModelMixin):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_user_profile = self.request.user.userprofile
        following = Follower.objects.filter(isFollowing=current_user_profile)
        return [followee.isFollowed for followee in following]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ToggleFollowView(GenericAPIView):
    queryset = UserProfile.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(UserProfile, id=user_id)      # gets the UserProfile object for the given user_id
        current_user_profile = request.user.userprofile

        follower_record, created = Follower.objects.get_or_create(
            isFollowed=user_to_follow,
            isFollowing=current_user_profile
        )

        if not created:
            follower_record.delete()
            return Response({'detail': 'Unfollowed successfully'}, status=status.HTTP_200_OK)

        return Response({'detail': 'Followed successfully'}, status=status.HTTP_201_CREATED)
