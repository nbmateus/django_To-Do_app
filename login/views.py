from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authLogin
from .forms import SignUpForm, LoginForm

from .models import User

def login(request):
    regForm = SignUpForm()
    logForm = LoginForm()
    tab = 'signIn'
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST' and request.POST['submit']=='register':
        regForm = SignUpForm(request.POST)
        tab = 'signUp'
        if regForm.is_valid():
            user = User.objects.create_user(username=regForm.cleaned_data.get('username'),password=regForm.clean_password2())
            user = authenticate(username=regForm.cleaned_data.get('username'), password=regForm.clean_password2())
            if user is not None:
                authLogin(request, user)
                return redirect('/')
    
    elif request.method == 'POST' and request.POST['submit']=='login':
        logForm = LoginForm(request.POST)
        if logForm.is_valid():
            user = User.objects.get(username = logForm.cleaned_data.get('username'))
            authLogin(request, user)
            return redirect('/')
    
    return render(request, 'login.html', {'regForm':regForm,'logForm':logForm, 'tab':tab})          
        
        

@csrf_exempt
def signUp(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        print("BUSCA EL VALOR DEL BOTON: "+str(request.POST))
        user = User.objects.create_user(username=form.cleaned_data.get('username'),password=form.clean_password2())
        user = authenticate(username=form.cleaned_data.get('username'), password=form.clean_password2())
        if user is not None:
            authLogin(request, user)
            return redirect('/')
    else:
         return redirect('/login/')

@csrf_exempt
def signIn(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        print("LOGIN FORM IS VALID")
        user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
        if user is not None:
            authLogin(request, user)
            return redirect('/')
    print("LOGIN FORM IS NOT VALID: "+str(form.errors))
    return redirect('/login/')

def signOut(request):
    logout(request)
    return redirect('/')
