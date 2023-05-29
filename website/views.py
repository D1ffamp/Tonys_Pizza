from django.views.generic import ListView, TemplateView
from django.shortcuts import render
from .models import Table, Booking


class TableListView(ListView):
    model = Table
    template_name = 'table_list.html'
    context_object_name = 'tables'
    # The 'model' attribute specifies the model to retrieve data from
    # The 'template_name' attribute specifies the template to render
    # The 'context_object_name' attribute specifies the name of
    #  the context variable in the template


class BookingListView(ListView):
    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'
    # The model attribute specifies the model to retrieve data from
    # The template_name attribute specifies the template to render
    # The context_object_name attribute specifies the name of the
    #  context variable in the template


class IndexView(TemplateView):
    template_name = 'index.html'
