from django.shortcuts import render

# Create your views here.
def viajes(request):
    return render(request, "viajes.html")
