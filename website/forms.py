from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    TIME_CHOICES = (
        ('9:00 AM', '9:00 AM'),
        ('10:00 AM', '10:00 AM'),
        ('11:00 AM', '11:00 AM'),
        ('12:00 PM', '12:00 PM'),
        ('1:00 PM', '1:00 PM'),
        ('2:00 PM', '2:00 PM'),
        ('3:00 PM', '3:00 PM'),
        ('4:00 PM', '4:00 PM'),
        ('5:00 PM', '5:00 PM'),
        ('6:00 PM', '6:00 PM'),
        ('7:00 PM', '7:00 PM'),
        ('8:00 PM', '8:00 PM'),
        ('9:00 PM', '9:00 PM'),
        ('10:00 PM', '10:00 PM'),
    )

    booking_time = forms.ChoiceField(choices=TIME_CHOICES)

    class Meta:
        model = Booking
        fields = ['user', 'table', 'date', 'time', 'num_guests']
