from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'num_guests']

class ReservationForm(forms.Form):
    name = forms.CharField(max_length=100)
    date = forms.DateField()
    time = forms.TimeField()
    num_guests = forms.IntegerField()