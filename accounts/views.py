from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserform
from .models import *
# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse
@login_required(login_url='/?')
def home(request):
    return render(request,'accounts/home.html')
@login_required(login_url='/?')
def contact(request):
   return render(request,'accounts/card.html')
def customer(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/home')
            else:
                messages.info(request,"USERNAME PASSWORD INCORRECT")

    context={}
    return render(request,'accounts/login1.html',context)

def out(request):
    logout(request)
    return redirect('/?')
def sign(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:

        form=CreateUserform()
        if request.method=='POST':
           form = CreateUserform(request.POST)
           if form.is_valid():
                 form.save()
                 us=form.cleaned_data.get('username')
                 messages.success(request,'ACCOUNT CREATED '+us)
                 return redirect('/?')

    context={'form':form}
    return render(request ,'accounts/register.html',context)