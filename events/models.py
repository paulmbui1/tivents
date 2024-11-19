from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class EventCategory(models.Model):
    """Dynamic event categories."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name="events")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    slug = models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Event.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class TicketType(models.Model):
    """Dynamic ticket types for events."""
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="ticket_types")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.name} ({self.price} KSH)"


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    booked_on = models.DateTimeField(auto_now_add=True)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="bookings")
    number_of_tickets = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Pending')

    def save(self, *args, **kwargs):
        # Calculate total price
        self.total_price = self.ticket_type.price * self.number_of_tickets
        # Reduce available tickets
        if self.pk is None:  # Only reduce for new bookings
            if self.ticket_type.available_quantity < self.number_of_tickets:
                raise ValueError("Not enough tickets available.")
            self.ticket_type.available_quantity -= self.number_of_tickets
            self.ticket_type.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} for {self.ticket_type.name} ({self.number_of_tickets} tickets) - {self.event.name} ({self.status})"
