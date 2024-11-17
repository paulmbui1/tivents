from django import forms
from .models import Booking, TicketType

class BookingForm(forms.ModelForm):
    ticket_type = forms.ModelChoiceField(
        queryset=TicketType.objects.none(),  # Dynamically loaded in the view
        widget=forms.Select(attrs={'class': 'form-control'})
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
