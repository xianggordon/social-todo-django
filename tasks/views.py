from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from splash.forms import createTaskForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
#tasks/views.py

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")
    
def newTask(request):
    if request.method == 'POST':
        form = createTaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            newTask = Task(owner=request.user, title=data['title'], description=data['description'])
            newTask.save()
            if User.objects.filter(username=data['collaborator1']).exists():
                newTask.collaborators.add(User.objects.get(username=data['collaborator1']))
            if User.objects.filter(username=data['collaborator2']).exists():
                newTask.collaborators.add(User.objects.get(username=data['collaborator1']))
            if User.objects.filter(username=data['collaborator3']).exists():
                newTask.collaborators.add(User.objects.get(username=data['collaborator1']))
                
    return HttpResponseRedirect('/')  

