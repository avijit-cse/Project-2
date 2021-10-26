from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    proile_pic=models.ImageField(upload_to='profile_pic',blank=True)
    fullname=models.CharField(max_length=264,blank=True)
    description=models.TextField(blank=True)
    dob=models.DateField(blank=True, null=True)
    website=models.URLField(blank=True)
    facebook=models.URLField(blank=True)

class follow(models.Model):
    follower=models.ForeignKey(User,on_delete=models.CASCADE,related_name='follower')
    following=models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')
    create_date=models.DateTimeField(auto_now_add=True)

    
    
    