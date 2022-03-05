from django.db import models
from django.contrib.auth.models import User

CITY_CHOICES = (
    ('Tashkent', 'Tashkent'),
    ('Samarkand', 'Samarkand'),
    ('Bukhara', 'Bukhara'),
    ('Nukus', 'Nukus'),
)

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, related_name='user')
    city = models.CharField(
        max_length=100, choices=CITY_CHOICES, null=True, blank=True)
    address = models.CharField(max_length=150, null=True, blank=True)
