from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


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
        return f'{self.date} {self.time}'
