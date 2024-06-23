from django.urls import path

from friendRequest.views import SendFriendRequestView

urlpatterns = [
    path('request/<int:user_id>/', SendFriendRequestView.as_view()),
]