from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'AgriInfoApp/index.html')

def update_profile(request):
    return render(request, 'AgriInfoApp/Update_Profile.html')

def logout(request):
    return render(request, 'AgriInfoApp/index.html')

def contact(request):
    return  render(request, 'AgriInfoApp/Contact.html')