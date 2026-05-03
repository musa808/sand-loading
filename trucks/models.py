from django.db import models
from accounts.models import User

class Truck(models.Model):
    plate_number = models.CharField(max_length=20)
    capacity_tons = models.FloatField()
    driver=models.CharField(max_length=100,null=True,blank=True)  # name of the driver

    def __str__(self):
        return self.plate_number