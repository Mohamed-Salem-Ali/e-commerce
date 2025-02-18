from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'core/home.html',context)


def cart(request):
    context={}
    return render(request,'core/cart.html')


def checkout(request):
    context={}
    return render(request,'core/checkout.html')