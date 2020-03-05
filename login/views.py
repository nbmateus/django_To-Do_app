from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authLogin
from .forms import SignUpForm, LoginForm

from .models import User

def login(request):
    if request.user.is_authenticated:
        return redirect('/')    
    return render(request, 'login.html', {'regForm':SignUpForm(),'logForm':LoginForm()})          
    


def signUp(request):
    regForm = SignUpForm(request.POST)
    response = {"redirectUrl":"/"}
    if regForm.is_valid():
        user = User.objects.create_user(username=regForm.cleaned_data.get('username'),password=regForm.clean_password2())
        authLogin(request, user)
        return JsonResponse(response)

    response["errors"] = regForm.errors
    return JsonResponse(response)


def signIn(request):
    logForm = LoginForm(request.POST)
    response = {"redirectUrl":"/"}
    if logForm.is_valid():
        user = User.objects.get(username = logForm.cleaned_data.get('username'))
        authLogin(request, user)
        return JsonResponse(response)

    response["errors"] = logForm.errors
    return JsonResponse(response)

def signOut(request):
    logout(request)
    return redirect('/')
