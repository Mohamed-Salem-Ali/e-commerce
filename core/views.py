from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def home(request):
    context={}
    return render(request,'core/home.html')


def cart(request):
    context={}
    return render(request,'core/cart.html')


def checkout(request):
    context={}
    return render(request,'core/checkout.html')