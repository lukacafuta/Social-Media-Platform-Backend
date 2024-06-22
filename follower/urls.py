from django.urls import path

from follower.views import ToggleFollowView, ListFollowersView, ListFollowingView

urlpatterns = [
    path('followers/', ListFollowersView.as_view()),
    path('following/', ListFollowingView.as_view()),
    path('toggle-follow/<int:user_id>/', ToggleFollowView.as_view()),
]