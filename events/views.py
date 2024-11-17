from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm
from .models import Event, Booking


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html'  , {'events': events}
                  )
def root(request):
    return render(request, "base.html")
# def event_detail(request, event_id):
#     return render(request, 'events/events_details.html', {'event': Event.objects.get(pk=event_id)})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.event = event
            booking.save()
            messages.success(request, "Your booking was successful!")
            return redirect('event_detail', event_id=event_id)
    else:
        form = BookingForm()
    return render(request, 'events/events_details.html', {'event': event, 'form': form})
