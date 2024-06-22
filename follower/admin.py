from django.contrib import admin
from .models import Follower


# Register your models here.
@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ('get_is_followed_username', 'get_is_following_username', 'dtCreated', 'dtUpdated')

    def get_is_followed_username(self, obj):
        return obj.isFollowed.username
    get_is_followed_username.short_description = 'Followed by'  # column name in admin interface

    def get_is_following_username(self, obj):
        return obj.isFollowing.username
    get_is_following_username.short_description = 'Following'   # column name in admin interface
