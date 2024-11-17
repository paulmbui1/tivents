from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Event, TicketType, Booking
from django.db.models import Q
from django.http import JsonResponse
from .models import TicketType


def event_list(request):
    events = Event.objects.order_by('-date')  # Order events by most recent first
    paginator = Paginator(events, 6)  # Show 6 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Fetch only the 5 most recent events for the slider
    recent_events = events[:5]

    return render(request, 'events/event_list.html', {
        'page_obj': page_obj,
        'recent_events': recent_events,
    })
def root(request):
    return render(request, "base.html")

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, event=event)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event  # Explicitly assign the event
            booking.user = request.user  # Assuming you want to associate the booking with the logged-in user
            try:
                booking.save()
                messages.success(request, "Booking successful!")
                return redirect('event_detail', event_id=event.id)
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = BookingForm(event=event)

    return render(request, 'events/events_details.html', {'event': event, 'form': form})


def get_ticket_price(request, ticket_type_id):
    ticket_type = get_object_or_404(TicketType, pk=ticket_type_id)
    return JsonResponse({'price': ticket_type.price})


def search_results(request):
    query = request.GET.get('q', '')
    events = Event.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)
    )

    paginator = Paginator(events, 9)  # Show 9 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'events/search_results.html', {
        'query': query,
        'events': page_obj,
    })