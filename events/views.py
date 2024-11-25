from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .forms import BookingForm, EventForm, SignUpForm, TicketTypeForm
from .models import Event, TicketType, Booking
from django.db.models import Q, ExpressionWrapper, F,FloatField
from django.http import JsonResponse, HttpResponse
from .models import TicketType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms import modelformset_factory, inlineformset_factory
from .models import EventCategory
from django.db.models import Sum, Count

from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

from django.http import FileResponse

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from pyzbar.pyzbar import decode
from PIL import Image
from django.utils.timezone import now

import qrcode
import base64
from io import BytesIO

def category_events(request, slug):
    category = get_object_or_404(EventCategory, slug=slug)
    events = Event.objects.filter(category=category)
    # Paginate events: 10 per page
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page')
    events = paginator.get_page(page_number)

    return render(request, 'events/category_events.html', {'category': category, 'events': events})

def root(request):
    events = Event.objects.order_by('-date')  # Order events by most recent first
    paginator = Paginator(events, 15)  # Show 15 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = EventCategory.objects.all()[:5]

    # Fetch only the 5 most recent events for the slider
    recent_events = events[:5]

    return render(request, 'events/event_list.html', {
        'page_obj': page_obj,
        'recent_events': recent_events,
        'categories': categories,
    })

def event_details(request, slug):
    event = get_object_or_404(Event, slug=slug)

    if request.method == 'POST':
        form = BookingForm(request.POST, event=event)
        if form.is_valid() :
            booking = form.save(commit=False)
            booking.event = event  # Explicitly assign the event
            booking.user = request.user  # Assuming you want to associate the booking with the logged-in user
            try:
                booking.save()
                receipt_url = reverse('download_receipt', kwargs={'booking_id': booking.id})
                success_message = f"Booking successful!<br> <a href='{receipt_url}'>Click here to download your receipt immediately.</a> <br>Be sure to save it"
                messages.success(request, success_message)
                return redirect('event_details', slug=slug)
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
    TicketFormSet = inlineformset_factory(
        Event,
        TicketType,
        form=TicketTypeForm,
        extra=1,
        can_delete=True
    )
    if request.method == "POST":
        event_form = EventForm(request.POST, request.FILES)
        formset = TicketFormSet(request.POST)

        if event_form.is_valid() and formset.is_valid():
            event = event_form.save(commit=False)
            event.user = request.user  # Assign current user
            event.save()
            formset.instance = event
            formset.save()
            return redirect('list_user_events')

    else:
        event_form = EventForm()
        formset = TicketFormSet()

    return render(
        request,
        'events/add_event.html',
        {
            'form': event_form,
            'formset': formset,
        }
    )

@login_required
def list_user_events(request):
    events = Event.objects.filter(user=request.user)
    context = {
        'events': events,
    }
    return render(request, 'events/user_events.html', context)

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

@login_required
def dashboard(request):
    user_events = Event.objects.filter(user=request.user)
    # Calculate metrics for the user's events
    total_bookings = Booking.objects.filter(event__in=user_events).count()  # Bookings for user's events
    total_revenue = Booking.objects.filter(event__in=user_events).aggregate(Sum('total_price'))['total_price__sum'] or 0
    event_metrics = user_events.annotate(
        total_bookings=Count('bookings'),
        remaining_tickets=Sum('ticket_types__available_quantity'),
        total_tickets = Sum('ticket_types__available_quantity') + Count('bookings', distinct=True),
    ).annotate(
        percentage_booked=ExpressionWrapper(
            F('total_bookings') * 100.0 / F('total_tickets'),
            output_field=FloatField()
        )
    )

    # Identify the most popular event by bookings
    most_popular_event = event_metrics.order_by('-total_bookings').first()

    context = {
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
        'event_metrics': event_metrics,
        'most_popular_event': most_popular_event,
    }
    return render(request, 'events/dashboard.html', context)


@login_required
def event_booking_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    bookings = Booking.objects.filter(event=event).order_by('-booked_on')


    context = {
        'event': event,
        'bookings': bookings,

    }
    return render(request, 'events/event_booking_details.html', context)


def generate_pdf_receipt(booking_id):
    from .models import Booking

    try:
        booking = Booking.objects.select_related('event', 'ticket_type').get(pk=booking_id)
    except Booking.DoesNotExist:
        return None

    # Generate QR Code
    qr_data = f"""
    Booking ID: {booking.id}
    Ticket ID: {booking.ticket_id}
    Event: {booking.event.name}
    Date: {booking.event.date}
    Location: {booking.event.location}
    Ticket Type: {booking.ticket_type.name}
    """
    qr = qrcode.QRCode(box_size=5, border=2)
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Save QR code to a BytesIO stream
    qr_stream = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_stream, format="PNG")
    qr_stream.seek(0)
    qr_code_base64 = base64.b64encode(qr_stream.getvalue()).decode('utf-8')

    context = {
        'booking': booking,
        'event': booking.event,
        'ticket_type': booking.ticket_type,
        'total_price': booking.total_price,
        'qr_code': qr_code_base64,  # Add QR code to the context
    }

    template = get_template('events/receipt.html')
    html = template.render(context)

    # Convert HTML to PDF
    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=buffer)

    if pisa_status.err:
        return None

    return buffer.getvalue()



def download_receipt(request, booking_id):
    pdf_content = generate_pdf_receipt(booking_id)

    if not pdf_content:
        return HttpResponse("Error generating PDF", content_type="text/plain")

    # Send the PDF as a downloadable file
    response = HttpResponse(pdf_content, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="receipt_{booking_id}.pdf"'
    return response


@login_required
@csrf_exempt
def update_booking_status(request):
    if request.method == "POST":
        booking_id = request.POST.get("booking_id")
        new_status = request.POST.get("status")

        try:
            booking = Booking.objects.get(id=booking_id, event__user=request.user)
            booking.status = new_status
            booking.save()
            return JsonResponse({"success": True, "message": "Status updated successfully."})
        except Booking.DoesNotExist:
            return JsonResponse({"success": False, "message": "Booking not found."})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request."})

@csrf_exempt
def delete_ticket(request, ticket_id):
    if request.method == 'POST' and request.user.is_authenticated:
        try:
            ticket = TicketType.objects.get(id=ticket_id)
            ticket.delete()
            return JsonResponse({'success': True})
        except TicketType.DoesNotExist:
            return JsonResponse({'error': 'Ticket not found'}, status=404)
    return JsonResponse({'error': 'Unauthorized'}, status=403)


@csrf_exempt
@login_required
def scan_qr_code(request):
    if request.method == "POST" and request.FILES.get('qr_code_image'):
        qr_code_image = request.FILES['qr_code_image']

        # Decode the QR code
        try:
            image = Image.open(qr_code_image)
            qr_data = decode(image)
            if not qr_data:
                return JsonResponse({"success": False, "message": "Invalid QR code."})

            decoded_data = qr_data[0].data.decode("utf-8")
            ticket_data = dict(line.split(": ") for line in decoded_data.split("\n"))

            ticket_id = ticket_data.get("ticket_id")
            event_name = ticket_data.get("event_name")

            # Validate ticket
            booking = get_object_or_404(Booking, ticket_id=ticket_id, event__name=event_name)
            if booking.ticket_is_scanned:
                return JsonResponse({"success": False, "message": "Ticket has already been scanned."})

            if booking.event.event_status != 'Upcoming':
                return JsonResponse({"success": False, "message": "Invalid ticket. Event is not upcoming."})

            # Update ticket status
            booking.ticket_is_scanned = True
            booking.save()

            return JsonResponse({"success": True, "message": "Ticket successfully validated."})

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})

    return JsonResponse({"success": False, "message": "Invalid request."})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@login_required
def scan_ticket_view(request):
    """Render the QR code scanning page."""
    return render(request, 'events/scan_ticket.html')

@csrf_exempt
@login_required
def verify_ticket(request):
    """Verify the scanned ticket."""
    if request.method == "POST":
        ticket_id = request.POST.get("ticket_id")  # Get ticket ID from the scanned QR code

        try:
            # Fetch the booking based on the ticket ID
            booking = Booking.objects.select_related('event').get(ticket_id=ticket_id)

            # Check if the event is valid and upcoming
            if booking.event.date < timezone.now().date():
                return JsonResponse({"success": False, "message": "This event has already expired."})

            if booking.ticket_is_scanned:
                return JsonResponse({"success": False, "message": "This ticket has already been scanned."})

            # Mark the ticket as scanned
            booking.ticket_is_scanned = True
            booking.save()

            # Return the scanned ticket information
            data = {
                "success": True,
                "message": "Ticket is valid and has been scanned successfully.",
                "ticket_details": {
                    "ticket_id": booking.ticket_id,
                    "event_name": booking.event.name,
                    "buyer_name": booking.name,
                    "buyer_email": booking.email,
                    "tickets_count": booking.number_of_tickets,
                }
            }
            return JsonResponse(data)

        except Booking.DoesNotExist:
            return JsonResponse({"success": False, "message": "Invalid ticket. Ticket not found."})

    return JsonResponse({"success": False, "message": "Invalid request method."})
