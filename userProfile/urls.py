from django.urls import path

from userProfile.views import UserListView, UserProfileDetailView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:id>/', UserProfileDetailView.as_view()),
]
