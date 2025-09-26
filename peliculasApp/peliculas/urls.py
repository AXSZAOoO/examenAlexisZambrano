from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_pelicula, name='agregar_pelicula'),
    path('lista/', views.listar_peliculas, name='listar_peliculas'),
    path('registro/', views.registro_usuario, name='registro'),
]