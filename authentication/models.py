from django.db import models
from django.contrib.auth.models import User
class Customer(models.Model):
    """
    Customer model that extends Django's built-in User model.
    Stores additional user details such as phone number.
    """
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE,# Deletes the Customer if the associated User is deleted
        unique=True
        ) 
    username = models.CharField(
        max_length=150, 
        unique=True # Ensures each username is unique
        )
    email = models.EmailField(
        unique=True # Ensure email is unique
        )  
    phone_number = models.CharField(
        max_length=15,
        blank=True, # Allows this field to be optional
        null=True # # Stores NULL in the database if not provided
        )

    def __str__(self):
        """
        Returns the username as a string representation of the Customer.
        
        """
        return self.username
