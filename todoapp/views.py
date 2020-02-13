from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as authLogin
from .admin import SignUpForm


from .models import Todo, User, UserManager
# Create your views here.

def todo(request):
    if request.user.is_authenticated:
        return render(request, 'todo.html', {'user':request.user})
    else:
        return redirect('/login/')
    

def getTodoList(request):
    return HttpResponse(serializers.serialize('json', Todo.objects.all().order_by('-pk')))

@csrf_exempt
def deleteTodo(request):
    Todo.objects.filter(id=request.POST["id"]).delete()
    return HttpResponse(202)

@csrf_exempt
def addTodo(request):
    done = True
    if(request.POST["done"] == 'false'):
       done = False

    newTodo = Todo.objects.create(todo=request.POST["todo"], done=done)
    newTodo.save()
    return HttpResponse(202)

@csrf_exempt
def updateTodo(request):
    done = True
    if(request.POST["done"] == 'false'):
       done = False

    Todo.objects.filter(id=request.POST["id"]).update(done=done)
    return HttpResponse(202)

def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    #else:
    #    if request.method == 'POST':
    #        form = SignUpForm(request.POST)
    #        if form.is_valid():
    #            userManager = UserManager()
    #            user = User.objects.create_user(username=form.cleaned_data.get('username'),password=form.clean_password2())
    #            user = authenticate(username=form.cleaned_data.get('username'), password=form.clean_password2())
    #            if user is not None:
    #                authLogin(request, user)
    #                return redirect('/')
    #    else:
    #        form = SignUpForm()

    #   return render(request, 'login.html', {'form':form})
    else:
        return render(request, 'login.html', {})

@csrf_exempt
def signUp(request):
    if request.POST["password1"] == request.POST["password2"]:
        user = User.objects.create_user(username=request.POST["username"],password=request.POST["password1"])

    if user:
        authLogin(request, user)
        return redirect('/')
    else:
         return redirect('/login/')

@csrf_exempt
def signIn(request):
    print("REQUEST: "+str(request))
    user = authenticate(username=request.POST["username"], password=request.POST["password"])
    if user is not None:
        print("ESTE ES EL USUARIO: "+str(user))
        authLogin(request, user)
        return redirect('/')
    else:
         return redirect('/login/')

def signOut(request):
    logout(request)
    return redirect('/')

