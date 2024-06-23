from django.db.models import Q
from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from userProfile.models import UserProfile
from userProfile.serializers import DetailedUserProfileSerializer


# Create your views here.
class UserListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DetailedUserProfileSerializer

    def get_queryset(self):
        search_string = self.request.query_params.get('search', None)
        if search_string:
            return UserProfile.objects.filter(
                Q(username__icontains=search_string)
            )
        return UserProfile.objects.all()


class UserProfileDetailView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = DetailedUserProfileSerializer
    lookup_field = 'id'
