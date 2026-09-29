from django.shortcuts import render

from .models import Juego


def inicio(request):
    return render(request, "app_games/inicio.html")


def catalogo(request):
    # select_related trae el género en la misma consulta (evita N+1 queries)
    # prefetch_related trae las plataformas (ManyToMany) en una segunda consulta optimizada
    juegos = Juego.objects.select_related("genero").prefetch_related("plataformas").all()
    return render(request, "app_games/catalogo.html", {"juegos": juegos})
