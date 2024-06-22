from django.urls import path

from comment.views import ListCreateCommentsView

urlpatterns = [
    path('<int:post_id>/', ListCreateCommentsView.as_view())
]
