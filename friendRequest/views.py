from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from friendRequest.models import FriendRequest
from friendRequest.serializers import FriendRequestSerializer, FriendRequestUpdateSerializer
from userProfile.models import UserProfile


# Create your views here.
class SendFriendRequestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        sender_profile = get_object_or_404(UserProfile, customUser=request.user)
        receiver_profile = get_object_or_404(UserProfile, customUser__id=user_id)

        data = {
            'sendRequestTo': sender_profile.id,
            'receivedBy': receiver_profile.id,
            'status': 'P'
        }
        serializer = FriendRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendRequestDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, friend_request_id):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        serializer = FriendRequestSerializer(friend_request)
        return Response(serializer.data)

    def patch(self, request, friend_request_id):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        serializer = FriendRequestUpdateSerializer(friend_request, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, friend_request_id):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        friend_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

