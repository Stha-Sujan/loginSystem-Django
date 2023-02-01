from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method == 'POST':
        usrname=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1 != password2:
            return HttpResponse("Password don't matched!!! ")
        else:
            user=User.objects.create_user(usrname,email,password1)
            user.save()
            print(usrname,email,password1,password2)
            return redirect('login')
    
    return render(request, 'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        usrname=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=usrname, password=password)
        print(usrname,password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password doesn't match!!! ")
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect ('login')