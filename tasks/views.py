from django.shortcuts import render
from django.http import HttpResponse
from tasks.models import Task
from splash.forms import newTaskForm
from django.contrib.auth.models import User

# Create your views here.
#tasks/views.py

def index(request):
    return HttpResponse("Hello, world. You're at the tasks index.")
    
def say_whatsup(request):
    return HttpResponse("Hello, WHAT IS UP?")