from django.shortcuts import render,redirect
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
                return redirect('/')
        else:
            messages.info(request,'Different Password')
            print('DIFFERENT PASSWORD')
            return redirect('register')
    else:
        return render(request,'register.html')