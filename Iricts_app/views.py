from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.core.paginator import Paginator
from math import*
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login
# Create your views here.

def home (request):
    df = employee.objects.all()
    df_paginator = Paginator(df,3)
    pagenum = request.GET.get('page')
    page = df_paginator.get_page(pagenum)
    context = {
        'page':page,
        'Total_No_Of_Page':ceil(df_paginator.count/3),
        'Total_No_Of_Value':df_paginator.count
    }
    return render(request,"index.html", context) 

def signup(request):
    if request.method == 'POST':
       First_name = request.POST['First_name']
       Last_name = request.POST['Last_name'] 
       username = request.POST['username'] 
       Email = request.POST['Email'] 
       Password1 = request.POST['Password1'] 
       Password2 = request.POST['Password2']
       
       
       if Password1 == Password2:

             if User.objects.filter(email = Email).exists():
                messages.info(request,"Email Allready Used by Another one")
                return redirect("signup")
             elif User.objects.filter(username=username).exists():
                messages.info(request,"User Allready used by another one")
                return redirect("signup")
             else:
                user = User.objects.create_user(first_name = First_name, last_name = Last_name, username=username, email = Email)
                user.save()
                return redirect("signin") 

       else:
            messages.info(request,"Didn't Match both password, Something went wrong")
            return redirect("signup")
    return render(request,"signup.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get['username']
        password = request.POST.get['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credetial")
            return redirect("signin")   


    return render(request,"signin.html")

def signout(request):
    return render(request,"signout.html")

def calculator(request):

    
    return render(request,"calc.html")

def add(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    add = n1+n2
    return render(request,'REsult.html',{'data':add})

def sub(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    sub = n1-n2
    return render(request,'REsult.html',{'data':sub})

def mult(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    mult = n1*n2
    return render(request,'REsult.html',{'data':mult})

def div(request):
    n1 = int(request.POST['num1'])
    n2 = int(request.POST['num2'])

    div = n1/n2
    return render(request,'REsult.html',{'data':div})