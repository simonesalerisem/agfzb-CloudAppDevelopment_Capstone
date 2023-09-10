from django.db import models
from django.utils.timezone import now


# Create your models here.

from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    # You can add any other fields you would like to include in car make model here
    # ...

    def __str__(self):
        return self.name

class CarModel(models.Model):
    SEDAN = 'SD'
    SUV = 'SV'
    WAGON = 'WG'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon'),
        # Add more types if needed
    ]

    car_make = models.ForeignKey(CarMake, related_name="car_models", on_delete=models.CASCADE)
    dealer_id = models.IntegerField() # assuming dealer_id is an integer
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    year = models.DateField()

    # You can add any other fields you would like to include in car model here
    # ...

    def __str__(self):
        return self.name

class CarDealer:

    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
