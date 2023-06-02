from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.

#Adding new Field to User Model using OneToOneField Relationship
class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   phone = models.CharField(max_length=32, blank=True, null=True)  
   country_of_residence = models.CharField(max_length=32, help_text='Country of Residence', null=True) 
   dob = models.DateField(help_text='Should be in yyyy-mm-dd format' ,blank=True, null=True) 

   gender = models.CharField(
        max_length=6, choices=(('Male', ('Male')), ('Female', ('Female')), ('Others', ('Others'))),
        blank=True, null=True) 

   relationship_status = models.CharField(
        max_length=20, choices=(('Married', ('Married')), ('Un_Married', ('Un Married')), ('In_A_Relation', ('In A Relation')), ('Complicated', ('Complicated')), ('single', ('Single'))),
        blank=True, null=True)  

   profession = models.CharField(max_length=32, help_text='Profession', blank=True, null=True)        

   bio = models.CharField(max_length=70, help_text='Enter your Bio (Must be between 60-70 characters)', blank=True, null=True)

   image = models.ImageField(default='default.jpg', upload_to='profile_pics')

   def __str__(self):
       return f'{self.user.username} Profile'

   #we are actually overwriting the existing save function of our class because, we want to resize images as they get uploaded to save space in our file system.  
   def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
             output_size = (300, 300)
             img.thumbnail(output_size)
             img.save(self.image.path)


class UserFollowing(models.Model):
   userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)  
   following = models.ManyToManyField(User)

   def __str__(self):
       return f'{self.userprofile.user.username} Followings'


class UserFollowers(models.Model):
   userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)  
   followers = models.ManyToManyField(User)

   def __str__(self):
       return f'{self.userprofile.user.username} Followers'


