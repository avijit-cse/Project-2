from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User


class post(models.Model):
    author= models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')
    image=models.ImageField(upload_to='post_image')
    caption= models.CharField(max_length=30,blank=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-upload_date']

class like(models.Model):
    
    post=models.ForeignKey(post,on_delete=models.CASCADE,related_name='liked_post')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='liker')
    date_create=models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}:{}'.format(self.user,self.post)



    

