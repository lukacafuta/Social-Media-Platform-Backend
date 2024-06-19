from django.db import models

from post.models import Post
from userProfile.models import UserProfile


# Create your models here.
class Comment(models.Model):
    #postCommented = models.F
    #username = models.CharField(max_length=100)
    creator = models.ForeignKey(to=UserProfile, related_name='comments', on_delete=models.CASCADE, default=1)
    text = models.TextField(max_length=255) # required
    #email = models.email()
    postCommented = models.ForeignKey(to=Post, related_name='comment', on_delete=models.CASCADE, default=1)
    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)
