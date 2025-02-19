import datetime
import json
from django.shortcuts import get_object_or_404, render
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

@login_required(login_url='login')
def processOrder(request):
    transaction_id = int(datetime.datetime.now().timestamp())
    data = json.loads(request.body)
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()


    ShippingAddress.objects.create(
    customer=customer,
    order=order,
    address=data['shipping']['address'],
    city=data['shipping']['city'],
    state=data['shipping']['state'],
    zipcode=data['shipping']['zipcode'],
    )
    return JsonResponse('Payment submitted..', safe=False)


def product_detail(request, product_id):
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items 
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product,'cartItems':cartItems}
    return render(request, 'core/product_detail.html', context)