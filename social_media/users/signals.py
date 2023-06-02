#This file signals.py is required to automatically instantiate a UserProfile automatically when a User model is created.

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, UserFollowing, UserFollowers

#signal to autocreate userprofile when user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()

#signal to autocreate userfollowing when useprofile is created
@receiver(post_save, sender=UserProfile)
def create_userfollowing(sender, instance, created, **kwargs):
    if created:
        UserFollowing.objects.create(userprofile=instance)


@receiver(post_save, sender=UserProfile)
def save_userfollowing(sender, instance, **kwargs):
    instance.userfollowing.save()


#signal to autocreate userfollowers when useprofile is created
@receiver(post_save, sender=UserProfile)
def create_userfollowers(sender, instance, created, **kwargs):
    if created:
        UserFollowers.objects.create(userprofile=instance)


@receiver(post_save, sender=UserProfile)
def save_userfollowers(sender, instance, **kwargs):
    instance.userfollowers.save()