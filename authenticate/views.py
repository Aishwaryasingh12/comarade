from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import RegisterForm
# Create your views here.
def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request, 'signup.html')