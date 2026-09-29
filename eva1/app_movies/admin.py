from django.contrib import admin

from .models import Director, Estreno, Pelicula


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre")
    search_fields = ("nombre",)


@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "director", "anio")
    search_fields = ("titulo", "director__nombre")
    list_filter = ("director", "anio")


@admin.register(Estreno)
class EstrenoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "fecha")
    search_fields = ("titulo", "fecha")
    list_filter = ("fecha",)
