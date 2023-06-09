from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Table(models.Model):
    """
    Model to represent a table in the restaurant.
    The string returns the table no
    """

    number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number}"


class Booking(models.Model):
    """
    Model to represent a booking made by a user.
    The meta class orders each booking by reservation date in descending order.
    str returns the reservation date and time to be used as booking title
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    num_guests = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"Booking {self.date} {self.time}"
