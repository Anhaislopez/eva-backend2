from django.contrib import admin

from .models import Genero, Juego, Plataforma


@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Plataforma)
class PlataformaAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "genero")
    search_fields = ("titulo", "genero__nombre")
    list_filter = ("genero", "plataformas")
    # filter_horizontal facilita asignar plataformas en la pantalla de edición
    filter_horizontal = ("plataformas",)
