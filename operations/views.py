from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Loading, TruckArrival
from trucks.models import Truck
from accounts.models import User
from accounts.sms import send_sms


@login_required
def loading_list(request):
    loads = Loading.objects.all().order_by('-created_at')
    return render(request, 'loading_list.html', {'loads': loads})


@login_required
def create_loading(request):
    if request.method == "POST":
        Loading.objects.create(
            truck_id=request.POST['truck'],
            material=request.POST['material'],
            loader=request.user,   # ✅ FIXED (NO STRING)
            quantity_tons=request.POST['quantity'],
            location=request.POST['location']
        )
        return redirect('loading_list')

    return render(request, 'create_loading.html', {
        'trucks': Truck.objects.all()
    })


@login_required
def create_arrival(request):
    if request.method == "POST":
        truck = get_object_or_404(Truck, id=request.POST['truck'])

        
        arrival = TruckArrival.objects.create(
            truck=truck,
            material=request.POST['material'],
            arrival_time=request.POST['arrival_time'],
            location=request.POST['location']
        )

        
        loaders = User.objects.filter(
            role="loader",
            phone_number__isnull=False
        ).exclude(phone_number="")

        phone_numbers = list(loaders.values_list("phone_number", flat=True))

        
        message = (
            f"🚛 Truck {truck.plate_number} will arrive at "
            f"{arrival.arrival_time} for {arrival.material} at {arrival.location}"
        )

        
        if phone_numbers:
            send_sms(message, phone_numbers)

        return redirect('loading_list')

    return render(request, "operations/create_arrival.html", {
        "trucks": Truck.objects.all()
    })