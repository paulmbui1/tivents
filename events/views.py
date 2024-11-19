from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .forms import BookingForm, EventForm, SignUpForm, TicketTypeForm
from .models import Event, TicketType, Booking
from django.db.models import Q
from django.http import JsonResponse
from .models import TicketType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelformset_factory


def event_list(request):
    events = Event.objects.order_by('-date')  # Order events by most recent first
    paginator = Paginator(events, 15)  # Show 6 events per page
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
        if form.is_valid() :
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

    paginator = Paginator(events, 15)  # Show 15 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'events/search_results.html', {
        'query': query,
        'events': page_obj,
    })

@login_required
def add_event(request):
    TicketFormSet = modelformset_factory(TicketType, form=TicketTypeForm, extra=0, can_delete=True)
    if request.method == "POST":
        event_form = EventForm(request.POST, request.FILES)
        formset = TicketFormSet(request.POST, queryset=TicketType.objects.none())
        if event_form.is_valid() and formset.is_valid():
            event = event_form.save(commit=False)
            event.user = request.user  # Assign the logged-in user
            event.save()
            tickets = formset.save(commit=False)
            for ticket in tickets:
                ticket.event = event
                ticket.save()
            messages.success(request, "Event created successfully!")
            return redirect('list_user_events')
    else:
        event_form = EventForm()
        formset = TicketFormSet(queryset=TicketType.objects.none())
    return render(request, 'events/add_event.html', {'form': event_form, 'formset': formset})

@login_required
def list_user_events(request):
    events = Event.objects.filter(user=request.user)
    return render(request, 'events/user_events.html', {'events': events})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect('list_user_events')
    return render(request, 'events/confirm_delete.html', {'event': event})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Hash the password
            user.save()
            login(request, user)  # Log the user in after signup
            return redirect('/events/my-events/')  # Redirect to my events page (or any page you want)
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk, user=request.user)  # Ensure user can only edit their events
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()  # Only updates fields that are changed
            return redirect('list_user_events')  # Redirect to the list of user's events
    else:
        form = EventForm(instance=event)  # Pre-fill the form with existing event data

    return render(request, 'events/edit_event.html', {'form': form, 'event': event})