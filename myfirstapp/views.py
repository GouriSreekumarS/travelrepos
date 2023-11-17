from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import place


# Create your views here.
def hello(request):
    obj = place.objects.all()
    return render(request, "index.html", {'result': obj})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid path")
            return redirect('login')

    return render(request, "login.html")


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cdpassword = request.POST['password1']
        if password == cdpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                                email=email,
                                                password=password)
                user.save();
                return redirect('login')
                print("Register Created")
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
