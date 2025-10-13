from django.http import HttpResponse
from django.shortcuts import render
from .models import User_details


def home(request):
    return HttpResponse("Hello, Django!")

def second(request):
    return render(request, 'second.html')

def user_details(request):
    users = User_details.objects.all()
    return render(request, 'user_details.html', {'users': users})

def third(request):
    a="hello welcome to django"
    return render(request, 'third.html', {'a': a})