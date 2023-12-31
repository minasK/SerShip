
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html",
                  {"form": form})


def logout_view (request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("/login/")

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/SerShip/")
    form = NewUserForm()
    return render(request, "register/register.html", {"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')  
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/SerShip/")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request, "registration/login.html", {"login_form": form})
