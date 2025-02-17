from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)  # Remove null=True, blank=True to enforce link
    username = models.CharField(max_length=150, unique=True)  # Replaces 'name', set unique=True
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
# Create your models here.