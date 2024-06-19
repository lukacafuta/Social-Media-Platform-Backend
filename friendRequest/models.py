from django.db import models

from userProfile.models import UserProfile


# Create your models here.
class FriendRequest(models.Model):

    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    #status = models.TextField(max_length=2)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    sendRequestTo = models.ForeignKey(to=UserProfile, related_name='requester', on_delete=models.CASCADE)
    #sendRequestTo = models.OneToOneField(to=User, on_delete=models.CASCADE)

    receivedBy = models.ForeignKey(to=UserProfile, related_name='receiver', on_delete=models.CASCADE)

    #creator = models.ForeignKey(to=UserProfile, related_name='posts', on_delete=models.CASCADE, default=1)
    #likedBy  = models.ManyToManyField(to=UserProfile, related_name='postsLiked', blank=True)
    #sharedBy = models.ManyToManyField(to=UserProfile, related_name='postsShared', blank=True)


    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)