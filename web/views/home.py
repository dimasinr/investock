from django.shortcuts import render

def login(request):
    return render(request, 'templates/auth/login.html')

def index(request):
    return render(request, 'templates/home/index.html')
