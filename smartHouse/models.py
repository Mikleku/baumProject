from __future__ import unicode_literals

from django.db import models

class room(models.Model):
    state=models.BooleanField()
    name = models.CharField(max_length=200)


# Create your models here.
