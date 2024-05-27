from django.urls import path
from . import views

app_name='parking_status'

urlpatterns = [
    path('parking_status/', views.parking_status, name='parking_status'),
]