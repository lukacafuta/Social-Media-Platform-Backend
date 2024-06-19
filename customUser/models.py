from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Field used for authentication
    USERNAME_FIELD = 'email'

    # Additional fields required when using createsuperuser (USERNAME_FIELD and passwords are always required)
    REQUIRED_FIELDS = ['username']

    # a single email can create only 1 account
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


"""
from django.db import models

# Create your models here.
class CustomUser(models.Model):
    text = models.TextField(max_length=255)  # required
    # email = models.email()
    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)
"""