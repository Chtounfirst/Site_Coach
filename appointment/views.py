from django.shortcuts import render

# Create your views here.
# appointment/views.py
from django.shortcuts import render, redirect
from .models import Appointment, Client

def home(request):
    return render(request, 'appointment/home.html')

def appointment(request):
    if request.method == 'POST':
        # Handle form submission
        client = Client(
            name=request.POST['name'],
            email=request.POST['email'],
        )
        client.save()
        
        appointment = Appointment(
            client=client,
            date_time=request.POST['date_time'],
        )
        appointment.save()
        
        return redirect('home')
    
    return render(request, 'appointment/appointment.html')

