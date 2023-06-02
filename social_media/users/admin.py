from django.contrib import admin
from .models import UserProfile, UserFollowing, UserFollowers

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(UserFollowing)
admin.site.register(UserFollowers)