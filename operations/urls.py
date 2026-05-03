from django.urls import path
from . import views

urlpatterns = [
    path('', views.loading_list, name='loading_list'),
    path('create/', views.create_loading, name='create_loading'),
]