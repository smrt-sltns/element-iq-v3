from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LoginForm

HOME_URL_NAME = "dashboard:home"  # "index"

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password)
            login(request, user)
            return redirect(HOME_URL_NAME)
    else:
        form = SignUpForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HOME_URL_NAME)
            user = authenticate(email=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(HOME_URL_NAME)
            context["errors"] = "Invalid Credentials"
    else:
        form = LoginForm()
    context["form"] = form
    return render(request, 'account/login.html', context)

def user_logout(request):
    logout(request)
    return redirect(HOME_URL_NAME)


