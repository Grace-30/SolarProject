from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class UserInput2(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    loadName=models.CharField(max_length=100)
    powerOfLoad =models.IntegerField(default=0)
    operatingHours= models.IntegerField(default=0)
    noOfLoad=models.IntegerField(default=0)
    effectiveSunlight= models.IntegerField(default=0)
   
    def __str__(self):
      return self.user.username
    
class UserInput(models.Model):
    userD= models.ManyToManyField(User)
    load_Name=models.CharField(max_length=100)
    power_Of_Load =models.IntegerField(default=0)
    operating_Hours= models.IntegerField(default=0)
    no_Of_Load=models.IntegerField(default=0)
    effective_Sunlight= models.IntegerField(default=0)

    def __str__(self):
      return self.load_Name

class ElectronicDetail(models.Model):
     userF= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
     electronicName= models.CharField(max_length=100)
     power_Of_Load =models.IntegerField(default=0)
     operating_Hours= models.IntegerField(default=0)
     no_Of_Load=models.IntegerField(default=0)
     effective_Sunlight= models.IntegerField(default=0)
      
     def __str__(self):
         return self.electronicName


