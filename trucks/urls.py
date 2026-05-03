from django.urls import path
from . import views

urlpatterns = [
    path('', views.truck_list, name='truck_list'),
    path('add/', views.add_truck, name='add_truck'),
    path('edit-truck/<int:id>/', views.edit_truck, name='edit_truck'),
    path('delete-truck/<int:id>/', views.delete_truck, name='delete_truck'),
]