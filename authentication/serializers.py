from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Customer

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'address']
        extra_kwargs = {
            'username': {'required': False},  # Make optional
            'email': {'required': False}  # Make optional
        }