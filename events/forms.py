from django import forms
from django.forms import inlineformset_factory
from .models import Booking, TicketType, Event


class BookingForm(forms.ModelForm):
    ticket_type = forms.ModelChoiceField(
        queryset=TicketType.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    number_of_tickets = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'ticket_type', 'number_of_tickets']

    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)
        if event:
            self.fields['ticket_type'].queryset = event.ticket_types.all()

    def clean_number_of_tickets(self):
        number_of_tickets = self.cleaned_data.get('number_of_tickets')
        ticket_type = self.cleaned_data.get('ticket_type')
        if ticket_type and number_of_tickets > ticket_type.available_quantity:
            raise forms.ValidationError(f"Only {ticket_type.available_quantity} tickets are available.")
        return number_of_tickets

#event form

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'category', 'date', 'time', 'location', 'image', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Location'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Event Description'}),
        }
TicketFormSet = inlineformset_factory(
    Event, TicketType,
    fields=['name', 'price', 'available_quantity'],
    extra=1,  # Number of empty ticket forms to display
    can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ticket Name'}),
        'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
        'available_quantity': forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Available Quantity'}),
    }
)
from django import forms
from django.contrib.auth.models import User

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
class TicketTypeForm(forms.ModelForm):
    class Meta:
        model = TicketType
        fields = ['name', 'price', 'available_quantity']
        widgets = {
            'price': forms.NumberInput(attrs={'step': '0.01'}),
            'available_quantity': forms.NumberInput(attrs={'min': 0}),
        }
