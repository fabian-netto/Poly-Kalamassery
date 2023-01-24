from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from app.forms import userform
from app.models import Customer

@login_required(login_url='register')
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        email = request.POST['email']
        psw = request.POST['psw']
        c =Customer.objects.create(uname=uname,email=email,psw=psw)
        c.save()
        return redirect(home)
    return render(request,'register.html') 