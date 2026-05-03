from django.shortcuts import render

def profile(request):
    return render(request, 'profile.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()

        login(request, user) 
        return redirect('/')

    return render(request, "register.html", {"form": form})


def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.user)
        return redirect('/')

    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')