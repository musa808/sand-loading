from django.shortcuts import render,redirect
from .models import Truck

def truck_list(request):
    trucks = Truck.objects.all()
    return render(request, 'truck_list.html', {'trucks': trucks})

from .forms import TruckForm

def add_truck(request):
    if request.method == "POST":
        form = TruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('truck_list')
    else:
        form = TruckForm()

    return render(request, 'add_truck.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Truck
from .forms import TruckForm

def edit_truck(request, id):
    truck = get_object_or_404(Truck, id=id)

    if request.method == "POST":
        form = TruckForm(request.POST, instance=truck)
        if form.is_valid():
            form.save()
            return redirect('truck_list')  # change to your list URL name
    else:
        form = TruckForm(instance=truck)

    return render(request, 'edit_truck.html', {'form': form})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Truck

def delete_truck(request, id):
    truck = get_object_or_404(Truck, id=id)

    if request.method == "POST":
        truck.delete()
        return redirect('truck_list')  

    return render(request, 'delete_truck.html', {'truck': truck})