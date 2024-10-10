from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request,'muesumproject.html')

def register(request):
    #test

    a = 10 +20
    b = 10

    if request.method == 'POST':
        username= request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username,password)
        user.save()
        return render(request,'register.html')
    return render(request,'register.html')

def loginPage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password') #name should be give in html input field to get this value here
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_authenticated:
                login(request,user)
                return redirect('/')
        else:
            return HttpResponse('This user is not active')
    else:
        return render(request,'login.html')


def new():
    return  True
