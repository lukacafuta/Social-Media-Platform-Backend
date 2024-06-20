from django.db import models

from post.models import Post

# Create your models here.
class Media(models.Model):
    urlMedia = models.CharField(max_length=255) # required
    #email = models.email()
    postRelated = models.ForeignKey(to=Post, related_name='medias', on_delete=models.CASCADE, default=1)
    dtCreated = models.DateTimeField(auto_now_add=True)
    dtUpdated = models.DateTimeField(auto_now=True)
