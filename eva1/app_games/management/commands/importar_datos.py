"""
Management command: importar_datos

Lee los archivos JSON existentes en static/data/ y los carga en la base de datos
usando get_or_create() para evitar duplicados si se ejecuta más de una vez.

Uso:
    python manage.py importar_datos
"""

import json
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from app_games.models import Genero, Juego, Plataforma
from app_movies.models import Director, Estreno, Pelicula


def _leer_json(nombre_archivo):
    """Lee y retorna el contenido de un archivo JSON en static/data/."""
    ruta = settings.BASE_DIR / "static" / "data" / nombre_archivo
    with ruta.open(encoding="utf-8") as f:
        return json.load(f)


class Command(BaseCommand):
    help = "Importa los datos iniciales desde los archivos JSON hacia la base de datos."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING("=== Iniciando importación de datos ==="))

        self._importar_juegos()
        self._importar_peliculas()
        self._importar_estrenos()

        self.stdout.write(self.style.SUCCESS("=== Importación completada ==="))

    # ------------------------------------------------------------------
    # Juegos
    # ------------------------------------------------------------------
    def _importar_juegos(self):
        self.stdout.write("\n→ Importando juegos...")
        datos = _leer_json("juegos.json")

        for item in datos:
            # 1. Género: get_or_create evita duplicados
            nombre_genero = item.get("genero", "Sin género").strip()
            genero, creado = Genero.objects.get_or_create(nombre=nombre_genero)
            if creado:
                self.stdout.write(f"  [+] Género creado: {genero}")

            # 2. Plataformas: el JSON las separa con " / "
            # Ej: "PC / Switch" → ["PC", "Switch"]
            plataformas_str = item.get("plataforma", "")
            nombres_plataformas = [p.strip() for p in plataformas_str.split("/") if p.strip()]

            plataformas_objs = []
            for nombre_plat in nombres_plataformas:
                plataforma, creado = Plataforma.objects.get_or_create(nombre=nombre_plat)
                if creado:
                    self.stdout.write(f"  [+] Plataforma creada: {plataforma}")
                plataformas_objs.append(plataforma)

            # 3. Juego: update_or_create usa el título como identificador
            juego, creado = Juego.objects.update_or_create(
                titulo=item["titulo"],
                defaults={
                    "genero": genero,
                    "descripcion": item.get("descripcion", ""),
                    "imagen": item.get("imagen", ""),
                },
            )

            # 4. Asignar plataformas (ManyToMany)
            juego.plataformas.set(plataformas_objs)

            accion = "creado" if creado else "actualizado"
            self.stdout.write(f"  [✓] Juego {accion}: {juego}")

    # ------------------------------------------------------------------
    # Películas
    # ------------------------------------------------------------------
    def _importar_peliculas(self):
        self.stdout.write("\n→ Importando películas...")
        datos = _leer_json("peliculas.json")

        for item in datos:
            # 1. Director: get_or_create evita duplicados
            nombre_director = item.get("director", "Desconocido").strip()
            director, creado = Director.objects.get_or_create(nombre=nombre_director)
            if creado:
                self.stdout.write(f"  [+] Director creado: {director}")

            # 2. Película
            pelicula, creado = Pelicula.objects.update_or_create(
                titulo=item["titulo"],
                defaults={
                    "director": director,
                    "anio": item.get("anio", 0),
                    "imagen": item.get("imagen", ""),
                },
            )

            accion = "creada" if creado else "actualizada"
            self.stdout.write(f"  [✓] Película {accion}: {pelicula}")

    # ------------------------------------------------------------------
    # Estrenos
    # ------------------------------------------------------------------
    def _importar_estrenos(self):
        self.stdout.write("\n→ Importando estrenos...")
        datos = _leer_json("estrenos.json")

        for item in datos:
            estreno, creado = Estreno.objects.update_or_create(
                titulo=item["titulo"],
                defaults={
                    "fecha": item.get("fecha", ""),
                    "recomendacion": item.get("recomendacion", ""),
                    "imagen": item.get("imagen", ""),
                },
            )

            accion = "creado" if creado else "actualizado"
            self.stdout.write(f"  [✓] Estreno {accion}: {estreno}")
