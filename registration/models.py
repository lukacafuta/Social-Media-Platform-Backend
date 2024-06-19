from django.db import models

from customUser.models import CustomUser


# Create your models here.
class Registration(models.Model):

    token = models.CharField(max_length=255)
    customUser = models.OneToOneField(to=CustomUser, related_name='registration', on_delete=models.CASCADE)

    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)
