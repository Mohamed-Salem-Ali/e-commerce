from django.shortcuts import render ,redirect
from django.contrib.auth.models import Group ,User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from core.models import Order
from .forms import CreateUserForm, CustomerForm
from .decrators import  unauthenticated_user
from .models import Customer

# -------------------------------------------
# User Registration View
# -------------------------------------------
@unauthenticated_user
def registerPage(request):
    """
    Handles user registration.

    """
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Assign user to 'customer' group
            group = Group.objects.get(name='customer')
            user.groups.add(group)

            # Create a Customer profile linked to the new user
            Customer.objects.create(
                user=user,
                username=user_name,
                email=email  
            )

            messages.success(request, 'User was created for '+user_name) 
            return redirect('login')
        
    context={'form': form}
    return render(request,'authentication/register.html',context)

# -------------------------------------------
# User Login View
# -------------------------------------------
@unauthenticated_user
def loginPage(request):
    """
    Handles user login.
    
    """
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'username or password is incorrect')
        
    context={}
    return render(request,'authentication/login.html',context)

# -------------------------------------------
# User Logout View
# -------------------------------------------
@login_required(login_url='login')
def logoutUser(request):
    """
    Logs out the user and redirects to login page.
    
    """
    logout(request)
    return redirect('login')

# -------------------------------------------
# User Profile View
# -------------------------------------------
@login_required(login_url='login')
def profile(request):
    """
    Displays and updates user profile.

    """
    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    cartItems = order.get_cart_items
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            new_username = form.cleaned_data.get('username')

            # Ensure username is unique before updating
            if User.objects.filter(username=new_username).exclude(id=request.user.id).exists():
                messages.error(request, 'This username is already taken')
            else:
                customer = form.save()  
                request.user.username = new_username  
                request.user.save()  
                messages.success(request, 'Profile updated successfully')

    context = {'form': form, 'order':order, 'cartItems':cartItems}
    return render(request, 'authentication/profile.html', context)