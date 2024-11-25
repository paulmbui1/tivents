import random
import secrets
import string

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from datetime import datetime, timedelta


class EventCategory(models.Model):
    """Dynamic event categories."""
    name = models.CharField(max_length=65, unique=True)
    description = models.TextField(blank=True, null=True)
    # slug = models.SlugField(unique=True, blank=True)
    slug = models.SlugField(max_length=65, unique=True)  # Previously max_length=255

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while EventCategory.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=65, db_index=False)
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name="events")
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=65)
    image = models.ImageField(upload_to='events/')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    slug = models.SlugField(unique=True, blank=True)

    event_status = models.CharField(
        max_length=20,
        choices=[
            ('Upcoming', 'Upcoming'),
            ('Expired', 'Expired'),
            ('Postponed', 'Postponed'),
            ('Canceled', 'Canceled'),
        ],
        default='Upcoming',
    )
    end_time = models.DateTimeField(null=True, blank=True)  # Optional end time for events


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.end_time and self.end_time < datetime.now():
            self.event_status = 'Expired'
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
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="ticket_types")
    name = models.CharField(max_length=65)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} - {self.event.name} ({self.price} KSH)"

import qrcode
from io import BytesIO
from django.core.files.base import ContentFile

class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='bookings') # name of event
    name = models.CharField(max_length=65) # name of buyer
    email = models.EmailField() # email of buyer
    phone = models.CharField(max_length=15, blank=True) # phone of buyer
    booked_on = models.DateTimeField(auto_now_add=True)
    ticket_type = models.ForeignKey(TicketType, on_delete=models.CASCADE, related_name="bookings")
    number_of_tickets = models.PositiveIntegerField()
    ticket_id = models.CharField(max_length=20, blank=True, unique=True) # random and unique ticket id for each buyer
    ticket_is_scanned = models.BooleanField(default=False) # check whether ticket is scanned
    ticket_qr_code = models.ImageField(upload_to="qr_codes/", blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled')
    ], default='Confirmed')

    def save(self, *args, **kwargs):
        # Calculate total price
        self.total_price = self.ticket_type.price * self.number_of_tickets

        # Generate ticket ID if not already set
        if not self.ticket_id:
            self.ticket_id = Booking.generate_unique_ticket_id()  # Call static method

        # Reduce available tickets
        if self.pk is None:  # Only reduce for new bookings
            if self.ticket_type.available_quantity < self.number_of_tickets:
                raise ValueError("Not enough tickets available.")
            self.ticket_type.available_quantity -= self.number_of_tickets
            self.ticket_type.save()

        # Generate QR code
        self.generate_qr_code()

        super().save(*args, **kwargs)


    @staticmethod
    def generate_unique_ticket_id():
        """Generate a unique 15-character alphanumeric ticket ID."""
        while True:
            ticket_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
            if not Booking.objects.filter(ticket_id=ticket_id).exists():
                return ticket_id
    def generate_qr_code(self):
        """Generates a QR code with booking information and saves it."""
        qr_data = {
            "ticket_id": self.ticket_id,
            "event_name": self.event.name,
            "buyer_name": self.name,
            "email": self.email,
            "phone": self.phone,
            "number_of_tickets": self.number_of_tickets,
            "total_price": str(self.total_price),
            "status": self.status,
        }
        qr_text = "\n".join(f"{key}: {value}" for key, value in qr_data.items())

        # Generate the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_text)
        qr.make(fit=True)

        # Convert to image
        img = qr.make_image(fill="black", back_color="white")

        # Save the image to a file-like object
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        # Save the file to the ImageField
        file_name = f"qr_{self.ticket_id}.png"
        self.ticket_qr_code.save(file_name, ContentFile(buffer.read()), save=False)
        buffer.close()

    def __str__(self):
        return f"{self.name} for {self.ticket_type.name} ({self.number_of_tickets} tickets) - {self.event.name} ({self.status})"


