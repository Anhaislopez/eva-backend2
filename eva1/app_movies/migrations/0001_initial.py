from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Director",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=200, unique=True)),
            ],
            options={
                "verbose_name": "Director",
                "verbose_name_plural": "Directores",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Pelicula",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                (
                    "director",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="peliculas",
                        to="app_movies.director",
                    ),
                ),
                ("anio", models.PositiveIntegerField(verbose_name="Año")),
                (
                    "imagen",
                    models.CharField(
                        blank=True,
                        help_text="Ruta relativa dentro de static/, ej: images/movies/mi-pelicula.svg",
                        max_length=300,
                    ),
                ),
            ],
            options={
                "verbose_name": "Película",
                "verbose_name_plural": "Películas",
                "ordering": ["titulo"],
            },
        ),
        migrations.CreateModel(
            name="Estreno",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                ("fecha", models.CharField(help_text="Ej: Octubre 2026", max_length=100)),
                ("recomendacion", models.TextField(blank=True)),
                (
                    "imagen",
                    models.CharField(
                        blank=True,
                        help_text="Ruta relativa dentro de static/, ej: images/movies/mi-estreno.svg",
                        max_length=300,
                    ),
                ),
            ],
            options={
                "verbose_name": "Estreno",
                "verbose_name_plural": "Estrenos",
                "ordering": ["titulo"],
            },
        ),
    ]
