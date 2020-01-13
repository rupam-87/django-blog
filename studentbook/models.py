from django.db import models
from datetime import date
# Create your models here.
class User(models.Model):
 username = models.TextField('User name',max_length=50)
 email = models.TextField('User email',max_length=50)
 password = models.TextField('User Password',max_length=60)

class Blog(models.Model):
 user_id=models.ForeignKey(User,on_delete=models.CASCADE)
 image=models.ImageField(upload_to='images/')
 discription=models.TextField('post discription')
 date=models.DateField(default=date.today)
 name=models.TextField('good name',max_length=20)