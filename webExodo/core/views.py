from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def login_view(request):
    return render(request, "core/login.html")

@login_required
def destinos(request):
    return render(request, "core/destinos.html")

