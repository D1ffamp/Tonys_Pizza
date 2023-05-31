from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, redirect, get_object_or_404
from .models import Table, Booking
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from django.urls import reverse_lazy


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


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'booking_list.html', {'bookings': bookings})


@login_required
def booking_create(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking-list')
    else:
        form = BookingForm()
    return render(request, 'booking_create.html', {'form': form})


@login_required
def booking_update(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking-list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'booking_update.html',
                  {'form': form, 'booking': booking})


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST':
        booking.delete()
        return redirect('booking-list')
    return render(request, 'booking_delete.html', {'booking': booking})


class BookingCreateView(CreateView):
    """
    A view that handles the creation of new bookings.

    Inherits from Django's CreateView class and provides the necessary
    attributes to customize its behavior.

    Attributes:
        template_name (str): The name of the template used to render the view.
        form_class (Form): The form used for creating the booking.
        success_url (str): The URL to redirect to after a successful
        form submission.
    """
    template_name = 'booking_create.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')


class BookingUpdateView(UpdateView):
    """
    A view that handles the updating of bookings.

    Inherits from Django's UpdateView class and provides the necessary
     attributes to customize its behavior.

    Attributes:
        template_name (str): The name of the template used to render
         the view ('booking_update.html').
        form_class (Form): The form used for updating
         the booking (BookingForm).
        success_url (str): The URL to redirect to after
         a successful form submission ('booking-list').
    """

    template_name = 'booking_update.html'
    form_class = BookingForm
    success_url = reverse_lazy('booking-list')


class BookingDeleteView(DeleteView):
    """
    A view that handles the deletion of bookings.

    Inherits from Django's DeleteView class and provides the necessary
     attributes to customize its behavior.

    Attributes:
        template_name (str): The name of the template used to
         render the view ('booking_delete.html').
        model (Model): The model to use for deleting the booking (Booking).
        success_url (str): The URL to redirect to
         after a successful deletion ('booking-list').
    """

    template_name = 'booking_delete.html'
    model = Booking
    success_url = reverse_lazy('booking-list')
