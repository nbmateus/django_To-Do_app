from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


from .models import Todo
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