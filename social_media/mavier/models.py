from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_counter = models.IntegerField()
    temp_like_flag = models.IntegerField(default=0) #this is the temp like flag used. If its 0 (False) it means that the current user hasn't liked this post, else if its 1 (True) it means the current user has liked this post
    comment_counter = models.IntegerField()
    share_counter = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app-post-detail', kwargs={'pk':self.pk})

class SharedPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    like_counter = models.IntegerField()
    temp_like_flag = models.IntegerField(default=0) #this is the temp like flag used. If its 0 (False) it means that the current user hasn't liked this post, else if its 1 (True) it means the current user has liked this post
    comment_counter = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app-sharedpost-detail', kwargs={'pk':self.pk})    


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(default=timezone.now)


class Like_for_SharedPost(models.Model):
    post = models.ForeignKey(SharedPost, on_delete=models.CASCADE)
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    date_liked = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment_content = models.TextField()

    def get_absolute_url(self):
        return reverse('app-comment-detail', kwargs={'pk':self.pk})


class Comment_forSharedPost(models.Model):
    post = models.ForeignKey(SharedPost, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment_content = models.TextField()

    def get_absolute_url(self):
        return reverse('app-sharedcomment-detail', kwargs={'pk':self.pk})


class Notifications(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification_type = models.CharField(
        max_length=100, choices=(('Post_Like', ('Post Like')), ('SharedPost_Like', ('SharedPost Like')), ('Post_Comment', ('Post Comment')), ('SharedPost_Comment', ('SharedPost Comment')), ('Post_Shared', ('Post_Shared')),('New_Follower', ('New_Follower'))),
        blank=True, null=True) 
    notification_date = models.DateTimeField(default=timezone.now)
    notification_message = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    link_variable = models.IntegerField(blank=True, null=True)
    sharedPOST = models.ForeignKey(SharedPost, on_delete=models.CASCADE, blank=True, null=True)
    





