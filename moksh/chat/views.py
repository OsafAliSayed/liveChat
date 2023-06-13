from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    return render(request, "chat/index.html")


def signin(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "chat/signin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "chat/signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST["username"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["cpassword"]
        if password != confirmation:
            return render(request, "chat/signup.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = None
            if 'isadmin' in request.POST:
                user = User.objects.create_user(username=username, password=password, isadmin=True)
            else:
                user = User.objects.create_user(username=username, password=password)
            user.save()
        except IntegrityError:
            return render(request, "chat/signup.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("signin"))
    else:
        return render(request, "chat/signup.html")
    

def signout(request):
    logout(request)
    return render(request, "chat/index.html")
