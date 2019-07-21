from django.db import models

# Create your models here.
class requestData(models.Model):
    First_Name = models.CharField(max_length=15)
    Middle_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Doctor_Name = models.CharField(max_length=15)
    Email = models.CharField(max_length=50)
    Time = models.CharField (max_length=20)