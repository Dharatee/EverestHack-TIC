from django.db import models

# Create your models here.
class doctorData(models.Model):
    First_Name = models.CharField(max_length=15)
    Middle_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Address = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Time = models.CharField (max_length=20)
    Availabilty = models.BooleanField()