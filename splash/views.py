from django.shortcuts import render
from django.http import HttpResponse
from .forms import newTaskForm
from django.contrib.auth.models import User
from tasks.models import Task
from django.db.models import Q
from .forms import loginForm
from .forms import RegisterForm
# Create your views here.

# def index(request):
#     return render(request, 'splash/index.html')
    
def index(request):
    if request.user.is_authenticated():
        tasks = Task.objects.filter(Q(owner=request.user) | Q(collaborators=request.user))
        return render(request, 'splash/index.html', {'user': request.user, 'new_task': newTaskForm, 'tasks': tasks})
    else:
        registerForm = RegisterForm()
        loginform = loginForm()
        return render(request, 'splash/index.html', {'login': loginform, 'register': registerForm})

    