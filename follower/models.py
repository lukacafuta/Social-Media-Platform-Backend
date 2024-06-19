from django.db import models

from userProfile.models import UserProfile


# Create your models here.
class Follower(models.Model):

    isFollowed = models.ForeignKey(to=UserProfile, related_name='follower', on_delete=models.CASCADE)
    # sendRequestTo = models.OneToOneField(to=User, on_delete=models.CASCADE)

    isFollowing = models.ForeignKey(to=UserProfile, related_name='followee', on_delete=models.CASCADE)

    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)

