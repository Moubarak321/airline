from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from urllib import request
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:   #si user not authentifié, rediriger vers la page de conexion
        return HttpResponseRedirect(reverse("login"))
    return render (request , "users/user.html")


def login_view(request):
    if request.method == "POST":
        username= request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password= password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "message": 'Eyinmi adjagô, pardon faut sciencer sur les id!!! On doit tout vous dire tchrrr  '
            })
    return render(request, "users/login.html")



def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "logged out."
    })