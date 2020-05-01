from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Arabic Language Web Application!!')

def login(request):
    return render(request,'login.html')

def home(request):
    return render(request,'home.html')


def listening(request):
    return render(request,'listening.html')
def reading(request):
    return render(request,'home.html')
def grammar(request):
    return render(request,'home.html')
def speaking(request):
    return render(request,'home.html')