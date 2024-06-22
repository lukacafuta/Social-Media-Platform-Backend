from rest_framework import status
from rest_framework.generics import GenericAPIView

from rest_framework.response import Response
from comment.models import Comment
from comment.serializers import CommentSerializer


# Create your views here.
class ListCreateCommentsView(GenericAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        return Comment.objects.filter(postCommented_id=post_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        post_id = self.kwargs.get('post_id')
        data = request.data.copy()      #make mutable copy of request data
        data['postCommented'] = post_id     #ensure the comment is linked to the correct post

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
