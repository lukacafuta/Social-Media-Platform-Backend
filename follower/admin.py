from django.contrib import admin

from .models import Follower

# Register your models here.
@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('isFollowed', 'isFollowing', 'dtCreated', 'dtUpdated')
