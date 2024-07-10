# travelapp/models.py
from django.db import models
from users.models import User

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    coordinates = models.CharField(max_length=50)
    image_url = models.URLField()

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    destinations = models.ManyToManyField(Destination)
    start_date = models.DateField()
    end_date = models.DateField()

class Accommodation(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Activity(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class DiningOption(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

class Budget(models.Model):
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    flights_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    accommodations_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    activities_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    dining_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

 