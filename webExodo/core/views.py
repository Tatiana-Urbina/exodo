from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def blog(request):
    return render(request, "core/blog.html")

def contacto(request):
    return render(request, "core/contacto.html")

def destinos(request):
    return render(request, "core/destinos.html")

