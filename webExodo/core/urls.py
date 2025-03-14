from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.blog, name="contacto"),
    path('destinos/', views.blog, name="destinos"),
]