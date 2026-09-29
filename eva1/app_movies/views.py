from django.shortcuts import render

from .models import Estreno, Pelicula


def cartelera(request):
    # select_related trae el director en la misma consulta SQL (JOIN)
    peliculas = Pelicula.objects.select_related("director").all()
    return render(request, "app_movies/cartelera.html", {"peliculas": peliculas})


def estrenos(request):
    estrenos_lista = Estreno.objects.all()
    return render(request, "app_movies/estrenos.html", {"estrenos": estrenos_lista})
