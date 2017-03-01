from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.



class Img(models.Model):
    img_path=models.CharField(max_length=200)
    img_class=models.CharField(max_length=200)



class Mark(models.Model):
    img =  models.ForeignKey(Img, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    tip = models.CharField(max_length=200,default='')
    value = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)




