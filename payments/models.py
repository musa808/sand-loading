from django.db import models
from operations.models import Loading

class Payment(models.Model):
    loading = models.OneToOneField(Loading, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    date_paid = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.loading} - {self.amount}"