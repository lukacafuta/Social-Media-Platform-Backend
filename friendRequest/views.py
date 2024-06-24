from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from friendRequest.models import FriendRequest
from friendRequest.serializers import FriendRequestSerializer, FriendRequestUpdateSerializer, FriendSerializer
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

            # send email to the receiver of the friend request
            send_mail(
                'Friend Request Received',
                f'Hi {receiver_profile.customUser.username}, you have received a friend request from {sender_profile.customUser.username}.',
                'luka.cafuta.dev@gmail.com',
                [receiver_profile.customUser.email],
                fail_silently=False,
            )

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
        original_status = friend_request.status
        serializer = FriendRequestUpdateSerializer(friend_request, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            updated_status = serializer.validated_data.get('status', original_status)

            if updated_status == 'A' and original_status != 'A':
                sender_profile = friend_request.sendRequestTo
                receiver_profile = friend_request.receivedBy

                message = f'Hi, {receiver_profile.customUser.username} has accepted your friend request.'

                send_mail(
                    'Friend Request Accepted',
                    message,
                    'luka.cafuta.dev@gmail.com',
                    [sender_profile.customUser.email],
                    fail_silently=False,
                )

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, friend_request_id):
        friend_request = get_object_or_404(FriendRequest, id=friend_request_id)
        friend_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AcceptedFriendsListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_profile = request.user.userprofile
        accepted_requests_sent = FriendRequest.objects.filter(sendRequestTo=user_profile, status='A')
        accepted_requests_received = FriendRequest.objects.filter(receivedBy=user_profile, status='A')

        friends_profiles = []
        # combine two query-sets into one
        all_accepted_requests = accepted_requests_sent.union(accepted_requests_received)

        # iterate over each friend request
        for req in all_accepted_requests:
            # check if the current user is the one who sent the request
            if req.sendRequestTo == user_profile:
                # the friend is the receiver of thew request
                friend_profile = req.receivedBy
            else:
                # the friend is the sender of the request
                friend_profile = req.sendRequestTo

            # add the friend profile to the list
            friends_profiles.append(friend_profile)

        serializer = FriendSerializer(friends_profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
