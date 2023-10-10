from django.db import models
from datetime import timedelta
from django.utils import timezone
# Create your models here.
def calculate_default_expected_date():
    # Calculate the default expected date as booking date + 7 days
    return timezone.now().date() + timedelta(days=7)
def calculate_default_booking_date():
    # Calculate the default expected date as booking date + 7 days
    return timezone.now().date()
class Info(models.Model):
    first_name=models.TextField(default='Hi')
    last_name=models.TextField(default='Hi') 
    username =models.TextField(default='Hi')
    email=models.EmailField(unique=True)
    password=models.TextField(default='Hi')
class Booking(models.Model):
    booking_user = models.CharField(max_length=100)
    sender_name = models.CharField(max_length=100)
    receiver_name = models.CharField(max_length=100)
    pickup_address = models.TextField()
    delivery_address = models.TextField()
    package_description = models.TextField()
    tracking_id = models.CharField(max_length=10)
    Current_Status=models.TextField(default="Booked")
    booking_date = models.DateField(default=calculate_default_booking_date)  # Date when the booking was made
    expected_date = models.DateField(default=calculate_default_expected_date)  # Expected delivery date

    def __str__(self):
        return f'Booking ID: {self.tracking_id}'

    class Meta:
        verbose_name_plural = 'Bookings'