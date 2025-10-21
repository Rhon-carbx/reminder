# Create your views here.
from django.shortcuts import render, redirect

# fake tasks for demo (you can connect a DB later)
tasks = [
    {"id": 1, "title": "Finish homework", "desc": "Math assignment"},
    {"id": 2, "title": "Buy groceries", "desc": "Milk, eggs"},
]

def login_view(request):
    return render(request, 'login.html')

def welcome(request):
    return render(request, 'users/all.html')

def edit_task(request):
    return render(request, 'edit_task.html')

def completed_tasks(request):
    return render(request, 'completed_tasks.html')

def about(request):
    return render(request, 'users/about.html')

def all(request):
    return render(request, 'users/all.html')

def add(request):
    return render(request, 'users/add.html')

def sign(request):
    return render(request, 'sign up.html')






