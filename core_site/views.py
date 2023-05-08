from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# # testing the index route
# def index(response) :
#     return HttpResponse("hola")

def index(response) :
        return render( response ,"index.html" , {}) 