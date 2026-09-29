from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genero",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Género",
                "verbose_name_plural": "Géneros",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Plataforma",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nombre", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "verbose_name": "Plataforma",
                "verbose_name_plural": "Plataformas",
                "ordering": ["nombre"],
            },
        ),
        migrations.CreateModel(
            name="Juego",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=200)),
                (
                    "genero",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="juegos",
                        to="app_games.genero",
                    ),
                ),
                (
                    "plataformas",
                    models.ManyToManyField(
                        blank=True,
                        related_name="juegos",
                        to="app_games.plataforma",
                    ),
                ),
                ("descripcion", models.TextField(blank=True)),
                (
                    "imagen",
                    models.CharField(
                        blank=True,
                        help_text="Ruta relativa dentro de static/, ej: images/games/mi-juego.svg",
                        max_length=300,
                    ),
                ),
            ],
            options={
                "verbose_name": "Juego",
                "verbose_name_plural": "Juegos",
                "ordering": ["titulo"],
            },
        ),
    ]
