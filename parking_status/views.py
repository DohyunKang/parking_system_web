from django.shortcuts import render

def parking_status(request):
    return render(request, 'parking_status/parking_status.html')