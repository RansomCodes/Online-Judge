from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['pass1']
        password2=request.POST['pass2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=firstname,last_name=lastname,password=password1) 
                user.save()
                print('User Created')
                return render(request,'login.html')
        else:
            messages.info(request,'Different Password')
            print('DIFFERENT PASSWORD')
            return redirect('register')
    else:
        return render(request,'register.html')
    
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credentials are Invalid')
            return redirect('login')
                
    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    home_url=reverse('home')
    return redirect(home_url)