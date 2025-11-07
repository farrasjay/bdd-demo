from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html", {"username": request.user.username})

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")

        if password != confirm:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("/login/")

    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("/login/")