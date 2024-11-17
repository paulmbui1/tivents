from django.contrib.auth.models import User
from django.db import models

class EventCategory(models.Model):
    """Dynamic event categories."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')
    def __str__(self):
        return f"{self.name} - {self.event.name} ({self.status})"
