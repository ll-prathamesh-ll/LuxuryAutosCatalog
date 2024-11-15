from django.db import models
from django.contrib.auth.models import User
from datetime import datetime  

now =  datetime.now()
time = now.strftime("%d %B %Y")
# Create your models here.


class Post(models.Model):
    postname = models.CharField(max_length=600)
    category = models.CharField(max_length=600)
    image = models.ImageField(upload_to='images/posts',blank=True,null=True)
    content = models.CharField(max_length=100000)
    time = models.CharField(default=time,max_length=100, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str( self.postname)  
    

class Contact(models.Model):
    name = models.CharField(max_length=600)
    email = models.EmailField(max_length=600)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000, blank=True)