from django.views.generic import ListView, TemplateView
from django.shortcuts import render, redirect
from .models import Table, Booking
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


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


@login_required  # Require authentication to access this view
def create_booking(request):
    if request.method == 'POST':
        # Retrieve form data
        customer_name = request.POST['customer_name']
        table_number = request.POST['table_number']
        booking_date = request.POST['booking_date']

        # Associate the booking with the logged-in user
        booking = Booking(
            customer_name=customer_name,
            table_number=table_number,
            booking_date=booking_date,
            user=request.user
        )
        booking.save()

        return redirect('booking-list')  # Redirect to the booking list page
    else:
        # Display the booking form template
        return render(request, 'booking_list.html')


@login_required  # Require authentication to access this view
def booking_list(request):
    # Fetch bookings associated with the currently logged-in user
    bookings = Booking.objects.filter(user=request.user)
    # Pass the bookings to the template
    return render(request, 'booking_list.html', {'bookings': bookings})
