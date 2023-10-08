from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class Item(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','X-Large'),
        ('XXL','XX-Large'),
        ('XXXL','XXX-Large'),
    )
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='items/')
    size = models.CharField(max_length=4, choices=SIZE_CHOICES, default='Small')

    def __str__(self):
        return f"Item created: {self.name}, {self.size} with price {self.price}€"
