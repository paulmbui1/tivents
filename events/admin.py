from django.contrib import admin
from .models import Event, Booking


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'time', 'location', 'image', 'description')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'event', 'booked_on', 'status')  # Customize fields to display in the admin list view
    search_fields = ('name', 'event__name')  # Enable search by user or event
    list_filter = ('status', 'booked_on')  # Filters for admin sidebar
    ordering = ('-booked_on',)  # Order by booking date (newest first)
    list_editable = ('status',)
