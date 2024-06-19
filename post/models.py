from django.db import models

from userProfile.models import UserProfile


# Create your models here.
class Post(models.Model):
    text = models.TextField(max_length=300)

    creator = models.ForeignKey(to=UserProfile, related_name='posts', on_delete=models.CASCADE, default=1)

    likedBy  = models.ManyToManyField(to=UserProfile, related_name='postsLiked', blank=True)
    sharedBy = models.ManyToManyField(to=UserProfile, related_name='postsShared', blank=True)


    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)