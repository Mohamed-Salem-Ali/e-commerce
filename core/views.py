import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from authentication.decrators import allowed_users

@login_required(login_url='login')
#@allowed_users(allowed_roles=['admin'])
def home(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    products = Product.objects.all()
    context = {'products':products,'items':items, 'order':order, 'cartItems':cartItems}
    return render(request,'core/home.html',context)

@login_required(login_url='login')
def cart(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'core/cart.html', context)

@login_required(login_url='login')
def checkout(request):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    items = order.orderitem_set.all()
    cartItems = order.get_cart_items      
    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'core/checkout.html', context)

@login_required(login_url='login')
def ordersPage(request):
    customer = request.user.customer  
    orders = Order.objects.filter(customer=customer).order_by('-date_ordered') 

    context = {
        'orders': orders,
    }
    return render(request, 'core/orders.html', context)



@login_required(login_url='login')
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)