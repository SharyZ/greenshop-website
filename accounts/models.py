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
        User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(
        max_length=50, help_text="Your phone number like: +998XXYYYYYYY", null=True, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile/', null=True, blank=True)


class Address(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField(
        max_length=100, choices=CITY_CHOICES, null=False)
    address = models.CharField(max_length=150, null=False)
    cart = models.ForeignKey('products.Cart', null=True,
                             blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.address
