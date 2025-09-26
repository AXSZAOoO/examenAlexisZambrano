from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Pelicula
from .forms import PeliculaForm

def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()

    return render(request, 'login/registro.html', {'form': form})

def listar_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'registrarPelicula/lista_pelicula.html', {'peliculas': peliculas})

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_peliculas')
    else:
        form = PeliculaForm()
    return render(request, 'login/agregar_pelicula.html', {'form': form})