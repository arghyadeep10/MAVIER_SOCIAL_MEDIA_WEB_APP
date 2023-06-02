from django.contrib import admin
from .models import Post, SharedPost, Like, Comment, Like_for_SharedPost, Comment_forSharedPost, Notifications
from users.models import UserProfile

# Register your models here.
admin.site.register(Post)
admin.site.register(SharedPost)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Like_for_SharedPost)
admin.site.register(Comment_forSharedPost)
admin.site.register(Notifications)
