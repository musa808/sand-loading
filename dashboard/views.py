from django.shortcuts import render
from trucks.models import Truck
from operations.models import Loading
from payments.models import Payment

def dashboard(request):
    context = {
        'trucks': Truck.objects.count(),
        'loads': Loading.objects.count(),
        'payments': Payment.objects.count(),
        'paid': Payment.objects.filter(is_paid=True).count(),
        'unpaid': Payment.objects.filter(is_paid=False).count(),
    }
    return render(request, 'dashboard/index.html', context)