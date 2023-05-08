from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# # testing the index route
# def index(response) :
#     return HttpResponse("hola")


def index(response):
    return render(response, "home.html", {})


def login_user(request):
    print(request.POST , request.POST.get("log") , "l \n\n")

    if request.method == "POST" and request.POST.get("log") == "log_out":
        logout(request)
        print("log out")
        return redirect('home')

    elif request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request ,username= username,password  =password)
        print(user)
        if user :
            login(request, user)
            messages.success(request , "you successfully signed")
            return redirect('home')
        else :
            if username : messages.error(request , "user name or password incorect ")
    return render(request, "login.html", {})


def logout_user(request):
    return render(request, "login.html", {})

def register(request):
    return render(request, "register.html")