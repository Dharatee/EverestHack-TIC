from django.db import models

# Create your models here.
class registration(models.Model):
    First_Name = models.CharField(max_length=15)
    Middle_Name = models.CharField(max_length=15)
    Last_Name = models.CharField(max_length=15)
    Username = models.CharField(max_length=15)
    Password = models.CharField(max_length=15)
    Email = models.CharField(max_length=52)
    Contact = models.BigIntegerField()
    Address = models.CharField(max_length=15)
    Blood_Group = models.CharField(max_length=5)