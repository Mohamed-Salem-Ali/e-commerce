from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Customer
from .serializers import UserProfileSerializer
# Create your views here.
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user