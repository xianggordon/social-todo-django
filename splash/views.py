from django.shortcuts import render
from django.http import HttpResponse
from .forms import newTaskForm
from django.contrib.auth.models import User
from tasks.models import Task
from django.db.models import Q
from .forms import loginForm
from .forms import registerForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as djangoLogin #login is already a function
from django.contrib.auth import logout as djangoLogout #logout is already a function
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    if request.user.is_authenticated():
        tasks = Task.objects.filter(Q(owner=request.user) | Q(collaborators=request.user))
        return render(request, 'splash/index.html', {'user': request.user, 'new_task': newTaskForm, 'tasks': tasks})
    else:
        return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm()})

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    if User.objects.filter(username=email).exists():
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                djangoLogin(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Error")
        else:
            return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Invalid password'})
    else:
        return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Invalid email address'})

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if len(data['fl_name']) > 50:
                return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Name too long'})

            if len(data['password']) > 50:
                return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Password too long'})

            if data['password'] == data['password_confirmation']:
                if User.objects.filter(username=data['email']).exists():
                    return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Account with this email already exists!'})
                else:
                    user = User.objects.create_user(data['email'], '', data['password'], first_name=data['fl_name'])
                    user = authenticate(username=data['email'], password=data['password'])
                    djangoLogin(request, user)
                    return HttpResponseRedirect('/')
            else:
                return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Passwords do not match'})
        else:
            return render(request, 'splash/index.html', {'login': loginForm(), 'register': registerForm(), 'errors': 'Name/e-mail/password too short'})

    return HttpResponseRedirect('/')
    
def logout(request):
    djangoLogout(request)
    return HttpResponseRedirect('/')