from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_driver = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    # add more profile fields as needed (documents, vehicle license, etc.)

class Bike(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bikes")
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    plate_number = models.CharField(max_length=32)
    capacity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

class Location(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class RideRequest(models.Model):
    rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="ride_requests")
    origin_lat = models.FloatField()
    origin_lng = models.FloatField()
    dest_lat = models.FloatField(null=True, blank=True)
    dest_lng = models.FloatField(null=True, blank=True)
    accepted = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Ride(models.Model):
    request = models.OneToOneField(RideRequest, on_delete=models.CASCADE, related_name="ride")
    driver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="rides")
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=32, choices=[
        ('requested','requested'),
        ('accepted','accepted'),
        ('on_trip','on_trip'),
        ('completed','completed'),
        ('canceled','canceled'),
    ], default='requested')
    fare = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

class Payment(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name="payment")
    stripe_charge_id = models.CharField(max_length=128, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name="rating")
    rater = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()  # 1-5
    comment = models.TextField(blank=True, null=True)
