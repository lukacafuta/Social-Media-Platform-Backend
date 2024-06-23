from django.urls import path

from friendRequest.views import SendFriendRequestView, FriendRequestDetailView

urlpatterns = [
    path('request/<int:user_id>/', SendFriendRequestView.as_view()),
    path('requests/<int:friend_request_id>/', FriendRequestDetailView.as_view()),
]