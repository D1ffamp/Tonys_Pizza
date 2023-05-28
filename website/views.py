from django.shortcuts import render
from .models import Table, Booking


def table_list(request):
    # Retrieve all tables from the database
    tables = Table.objects.all()

    # Render the 'table_list.html' template with the tables data
    return render(request, 'table_list.html', {'tables': tables})


def booking_list(request):
    # Retrieve all bookings from the database
    bookings = Booking.objects.all()

    # Render the 'booking_list.html' template with the bookings data
    return render(request, 'booking_list.html', {'bookings': bookings})
