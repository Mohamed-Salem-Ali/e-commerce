from django.contrib.auth.models import AbstractUser ,Group,Permission
from django.db import models
class Customer(AbstractUser):
    email = models.EmailField(unique=False)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username