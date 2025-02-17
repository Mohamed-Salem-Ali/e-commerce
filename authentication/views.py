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
    
def register(request):
    context={}
    return render(request,'authentication/register.html')


def login(request):
    context={}
    return render(request,'authentication/login.html')


def profile(request):
    context={}
    return render(request,'authentication/profile.html')