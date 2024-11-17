from django.shortcuts import render
from .models import Event

def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html'  , {'events': events}
                  )
def root(request):
    return render(request, "base.html")
def event_detail(request, event_id):
    return render(request, 'events/events_details.html', {'event': Event.objects.get(pk=event_id)})