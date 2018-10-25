from django.db import models
from django.contrib import admin


# Create your models here.
class HelloT(models.Model):
    name = models.CharField(max_length= 20)
    title = models.CharField(max_length= 20)
    def __unicode__(self):
     return self.name
