from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from .models import Table, Booking


class TableListView(ListView):
    model = Table
    template_name = 'table_list.html'
    context_object_name = 'tables'


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'


class IndexView(TemplateView):
    template_name = 'index.html'
