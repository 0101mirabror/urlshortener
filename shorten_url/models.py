from django.db import models
from django.forms import URLField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30, null=False, error_messages={'name':'Ismingizni kiriting'})
    email = models.EmailField(max_length=50,null=False, error_messages={'email':"Emailingizni 'example@gmail.com' shaklida kiriting"})
    message = models.TextField(max_length=5000, null=False, error_messages={'message':"Enter message"})
    created_time = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

class Report(models.Model):
    
    shorturl = models.URLField(max_length=100, null=False)
    message = models.TextField(max_length=1000)
    email = models.EmailField(max_length=200)
    objects = models.Manager()
    
    def __str__(self):
        return self.email