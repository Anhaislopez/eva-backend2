from django.db import models


class Director(models.Model):
    nombre = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directores"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    # Un director puede tener varias películas → ForeignKey
    director = models.ForeignKey(
        Director,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="peliculas",
    )
    anio = models.PositiveIntegerField(verbose_name="Año")
    imagen = models.CharField(
        max_length=300,
        blank=True,
        help_text="Ruta relativa dentro de static/, ej: images/movies/mi-pelicula.svg",
    )

    class Meta:
        verbose_name = "Película"
        verbose_name_plural = "Películas"
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} ({self.anio})"


class Estreno(models.Model):
    titulo = models.CharField(max_length=200)
    fecha = models.CharField(
        max_length=100,
        help_text="Ej: Octubre 2026",
    )
    recomendacion = models.TextField(blank=True)
    imagen = models.CharField(
        max_length=300,
        blank=True,
        help_text="Ruta relativa dentro de static/, ej: images/movies/mi-estreno.svg",
    )

    class Meta:
        verbose_name = "Estreno"
        verbose_name_plural = "Estrenos"
        ordering = ["titulo"]

    def __str__(self):
        return f"{self.titulo} — {self.fecha}"
