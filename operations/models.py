from django.db import models
from trucks.models import Truck
from accounts.models import User



class Loading(models.Model):
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    material = models.CharField(max_length=50, default="sand")
    
    loader = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': 'loader'}
    )

    quantity_tons = models.FloatField()
    location = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.truck.plate_number} - {self.material} ({self.quantity_tons} tons)"


class TruckArrival(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('notified', 'Notified'),
        ('arrived', 'Arrived'),
    )

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    material = models.CharField(max_length=50, default="sand")
    
    arrival_time = models.DateTimeField()
    location = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.truck.plate_number} arriving at {self.arrival_time}"