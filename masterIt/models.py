from django.db import models
from cities_light.models import Country, Region, City

# Create your models here.
class TryIterables(models.Model):
	SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        )
	name = models.CharField(max_length=60)
	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

from address.models import AddressField
class TestAddress(models.Model):
    address = AddressField()

class CountryStateCity(models.Model):
    """Practice to validate country, state, city data"""
    country = models.ForeignKey(Country)
    region = models.ForeignKey(Region)
    city = models.ForeignKey(City)
