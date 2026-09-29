from django.db import models


class Genero(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Género"
        verbose_name_plural = "Géneros"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Plataforma(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Plataforma"
        verbose_name_plural = "Plataformas"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    # Varios juegos pueden compartir el mismo género → ForeignKey
    genero = models.ForeignKey(
        Genero,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="juegos",
    )
    # Un juego puede estar en varias plataformas y viceversa → ManyToManyField
    plataformas = models.ManyToManyField(
        Plataforma,
        blank=True,
        related_name="juegos",
    )
    descripcion = models.TextField(blank=True)
    imagen = models.CharField(
        max_length=300,
        blank=True,
        help_text="Ruta relativa dentro de static/, ej: images/games/mi-juego.svg",
    )

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo
