from django.shortcuts import render
from django.shortcuts import render, redirect

def index(request):
    return render(request, 'home/index.html')
def before_index(request):
    return render(request, 'home/before_index.html')

