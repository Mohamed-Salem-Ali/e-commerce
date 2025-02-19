from pyexpat.errors import messages
from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:  
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user_name = form.cleaned_data.get('username')
                messages.success(request, 'User was created for '+user_name) 

                return redirect('login')
        context={'form': form}
        return render(request,'authentication/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:  
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