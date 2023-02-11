from django.db import models

# Create your models here.
# appointment/models.py
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

