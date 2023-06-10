from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# # testing the index route
# def index(response) :
#     return HttpResponse("hola")

from .models import Records
from .forms import signup_form ,AddRecord_form

def index(response):
    records = Records.objects.all()
    print("\n\n\n recors" , Records, "\n\n")
    return render(response, "home.html", {"records" :records})


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

    if request.method == "POST" :
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            pasword = form.cleaned_data["password1"]
            
            user =authenticate(username=username, pasword = pasword)
            login(request, user)
            messages.success(request , "you have successfuly sign up")
            return redirect('home')
        else :print(" not valid \n\n\\n" , form.errors)
    else : 
        form = signup_form()
        return render(request, "register.html" , {"form" :form})
    return render(request, 'register.html', {'form':form})


def customer_records (requests, id):

    print(id)

    if requests.method == "POST" :
        print(requests.POST)
        action = requests.POST.get('action')

        if action == 'cancel':
            return redirect('home')
        if action == 'save':
            current_record = Records.objects.get(id=id)
            form = AddRecord_form(requests.POST or None , instance=current_record)
            if form.is_valid():
                form.save()
                messages.success(requests,f"record {current_record.firstname} have been updated  ")
                return redirect('home')

            return redirect('home')
        if action == 'delete':
            records = Records.objects.get(id=id)
            records.delete()
            messages.success(requests,f"you have removed records of { records.firstname }")
            return redirect('home')
    records = Records.objects.get(id=id)
    print(records)
    if requests.user.is_authenticated:
        return render(requests , 'customer_records.html' , {"records" : records})
    
    else:
        messages.error(requests , "you should be logged in to view a customer record")
        return redirect('home')

def add_records(request):
    form = AddRecord_form( request.POST or None)
    if request.user.is_authenticated:

        if request.method == 'POST' and form.is_valid():
            
            # print( " \n\n\n\n post val", request.POST)
            form.save()
            messages.success(request, 'New form has been added ')
            return redirect('home')

        return render(request , "add_record.html" , {"form" :form})
    
    else :
        messages.error(request ,"you have to log in to add new records")
        return redirect('home')