from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import *
def login(request):
    if request.session.has_key('is_logged'):
        return redirect('home')
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        count = User.objects.filter(email=email,password=password).count()
        if count> 0:
          request.session['is_logged'] = True
          return redirect('home')
        else:
          messages.error(request,"invalid password or email")
          return redirect('login')

    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def register_user(request):
    if request.POST:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        count = User.objects.filter(email=email).count()
        if count>0:
            messages.info(request,'user already exsits')
            return redirect('signup')
        else:
            obj = User(username=username, email=email,password=password)
            obj.save()
            messages.success(request,"u are succesfully register")
            return redirect('login')

def home(request):
    if request.session.has_key('is_logged'):
        fetch_data=Blog.objects.all()
        return render(request,'home.html',{'data':fetch_data})
    return redirect('login')
def logout(request):
    del request.session['is_logged']
    return redirect('login')
def post(request):
    if request.POST:
         pass
    return render(request,'post.html')
