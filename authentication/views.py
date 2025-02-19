from pyexpat.errors import messages
from django.shortcuts import render ,redirect
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decrators import unauthenticated_user
from .models import Customer

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            user_name = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                username=user_name,
                email=email  # Ensure email is saved
            )
            messages.success(request, 'User was created for '+user_name) 

            return redirect('login')
    context={'form': form}
    return render(request,'authentication/register.html',context)

@unauthenticated_user
def loginPage(request):
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

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def profile(request):
    context={}
    return render(request,'authentication/profile.html')