from django.db import models

# Create your models here.


class MarketModel(models.Model):
    name=models.CharField(max_length=200,unique=True,blank=True,null=True)
    location=models.CharField(max_length=200,default="Feni")
    def __str__(self):
       return self.name
   