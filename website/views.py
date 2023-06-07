from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from allauth.account.views import LoginView  # Import LoginView from allauth
from .forms import BookingForm
from .models import Table, Booking


class TableListView(ListView):
    """
    A view that lists all the tables.

    Inherits from Django's ListView class to provide
    a list view for the tables.
    """

    model = Table
    template_name = 'table_list.html'
    context_object_name = 'tables'


class BookingListView(LoginRequiredMixin, ListView):
    """
    A view that lists the bookings for the authenticated user.

    Inherits from Django's ListView class to provide a list view for the
    bookings.
    Requires the user to be logged in.

    Attributes:
        model (Model): The model to use for the list view (Booking).
        template_name (str): The name of the template used to render the view.
        context_object_name (str): The name of the variable to use in the
        template for the bookings.
    """

    model = Booking
    template_name = 'booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        """
        Returns the queryset of bookings for the authenticated user.
        """
        return Booking.objects.filter(user=self.request.user)


class IndexView(TemplateView):
    """
    A view that renders the index page.

    Inherits from Django's TemplateView class to provide a simple template view for the index page.

    Attributes:
        template_name (str): The name of the template used to render the view.
    """

    template_name = 'index.html'


class CustomLoginView(LoginView):
    """
    A view that handles user authentication and login.

    Inherits from the LoginView provided by AllAuth to provide a customized login view.

    Attributes:
        template_name (str): The name of the template used to render the view ('login.html').
    """

    template_name = 'login.html'


class BookingCreateView(LoginRequiredMixin, CreateView):
    """
    A view that handles the creation of new bookings.

    Inherits from Django's CreateView class and provides the necessary attributes to customize its behavior.

    Attributes:
        model (Model): The model to use for creating the booking (Booking).
        form_class (Form): The form used for creating the booking (BookingForm).
        template_name (str): The name of the template used to render the view.
        success_url (str): The URL to redirect to after a successful form submission ('booking-list').
    """

    model = Booking
    form_class = BookingForm
    template_name = 'booking_create.html'
    success_url = reverse_lazy('booking-list')

    def form_valid(self, form):
        """
        Saves the form and sets the user of the booking to the authenticated user.
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookingUpdateView(LoginRequiredMixin, UpdateView):
    """
    A view that handles the updating of bookings.

    Inherits from Django's UpdateView class and provides the necessary attributes to customize its behavior.

    Attributes:
        model (Model): The model to use for updating the booking (Booking).
        form_class (Form): The form used for updating the booking (BookingForm).
        template_name (str): The name of the template used to render the view.
        success_url (str): The URL to redirect to after a successful form submission ('booking-list').
    """

    model = Booking
    form_class = BookingForm
    template_name = 'booking_update.html'
    success_url = reverse_lazy('booking-list')

    def get_queryset(self):
        """
        Returns the queryset of bookings for the authenticated user.
        """
        return super().get_queryset().filter(user=self.request.user)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    """
    A view that handles the deletion of bookings.

    Inherits from Django's DeleteView class and provides
    the necessary attributes to customize its behavior.

    Attributes:
        model (Model): The model to use for deleting the booking (Booking).
        template_name (str): The name of the template used to render the view.
        success_url (str): The URL to redirect to after a successful deletion ('booking-list').
    """

    model = Booking
    template_name = 'booking_delete.html'
    success_url = reverse_lazy('booking-list')

    def get_queryset(self):
        """
        Returns the queryset of bookings for the authenticated user.
        """
        return super().get_queryset().filter(user=self.request.user)


class ReservationView(LoginRequiredMixin, TemplateView):
    template_name = 'reservation.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookingForm()
        return context

    def post(self, request, *args, **kwargs):
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return redirect('booking-list')
        return self.render_to_response({'form': form})
