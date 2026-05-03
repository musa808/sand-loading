from django import forms
from .models import Truck

class TruckForm(forms.ModelForm):
    class Meta:
        model = Truck
        fields = ['plate_number', 'capacity_tons', 'driver']