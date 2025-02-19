import datetime
import json
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
from authentication.decrators import allowed_users
# paypal
from django.urls import  reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid #

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
    total = order.get_cart_total
    host = request.get_host()
    # PayPal Payment Data
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': total,
        'item_name': 'Order',
        'no_shipping': '2',
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse("paypal-ipn")),
        'return_url': 'http://{}{}'.format(host, reverse("payment_success")),
        'cancel_return': 'http://{}{}'.format(host, reverse("payment_failed")),
    }
    paypal_form = PayPalPaymentsForm(initial=paypal_dict)
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'paypal_form': paypal_form}
    return render(request, 'core/checkout.html', context)

@login_required(login_url='login')
def ordersPage(request):
    customer = request.user.customer  
    orders = Order.objects.filter(customer=customer).order_by('-date_ordered') 
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items

    context = {
        'orders': orders,
        'cartItems': cartItems
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

def payment_success(request):
    return render(request,"core/payment_success.html")

def payment_failed(request):
    return render(request,"core/payment_failed.html")
