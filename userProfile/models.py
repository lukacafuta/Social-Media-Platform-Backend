from django.db import models

from customUser.models import CustomUser

# Create your models here.
class UserProfile(models.Model):
    #postCommented = models.F
    username = models.CharField(max_length=100, unique=True)    # username must be unique
    avatar = models.CharField(max_length=255, blank=True, null=True)    # optional
    background = models.CharField(max_length=255, blank=True, null=True)    # optional
    birthdate = models.DateField(blank=True, null=True) # optional

    customUser = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)

    #postCommented = models.ForeignKey(to=Post, related_name='comment', on_delete=models.CASCADE, default=1)
    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
