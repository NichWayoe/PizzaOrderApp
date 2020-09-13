from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message":None})
    context = {
        "user":request.user
    }
    return render(request, "orders/index.html", context)

def login_view(request):
    username = request.POST['Username']
    password = request.POST['Password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    return render(request, "orders/login.html", {"message":"invalid credentials"})
   
def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message":None})

def sign_up_view(request):
    username = request.POST['Username']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['']