from django.urls import path
from . import views

urlpatterns = [
    path('viajes/', views.viajes, name="viajes"),
]