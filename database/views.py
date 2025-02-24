from django.shortcuts import render

# Create your views here.


def signup(request):
    return render(request,'signup')

def login(request):
    return render(request,'login')

def index(request):
    return render(request,'index')

