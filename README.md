# Portal Geek & Dev

## Descripción

Portal web desarrollado con Django que integra dos módulos principales:

- **Videojuegos**: catálogo de juegos indie con géneros y plataformas.
- **Películas y Estrenos**: cartelera geek y próximos estrenos con recomendaciones.

La aplicación utiliza una base de datos relacional (MySQL/MariaDB) gestionada mediante Django ORM. El CRUD completo se administra desde Django Admin. Los datos iniciales se cargan desde archivos JSON mediante un management command propio.

---

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3.12+ | Lenguaje principal |
| Django 5.2 | Framework web |
| MySQL / MariaDB | Base de datos relacional |
| Django ORM | Consultas a la base de datos |
| Django Admin | CRUD de todos los modelos |
| Bootstrap 5 | Estilos y componentes UI |
| python-dotenv | Variables de entorno |
| Git / GitHub | Control de versiones |

---

## Aplicaciones

### app_games

Gestiona el catálogo de videojuegos.

**Modelos:**

- `Genero` — nombre único. Un género puede agrupar varios juegos.
- `Plataforma` — nombre único. Una plataforma puede tener varios juegos.
- `Juego` — título, género (ForeignKey), plataformas (ManyToManyField), descripción e imagen.

**Relaciones:**
- `Juego → Genero`: ForeignKey, porque varios juegos pueden compartir el mismo género.
- `Juego ↔ Plataforma`: ManyToManyField, porque un juego puede estar en varias plataformas y una plataforma puede tener varios juegos.

### app_movies

Gestiona la cartelera y los próximos estrenos.

**Modelos:**

- `Director` — nombre único.
- `Pelicula` — título, director (ForeignKey), año e imagen.
- `Estreno` — título, fecha, recomendación e imagen.

**Relaciones:**
- `Pelicula → Director`: ForeignKey, porque un director puede tener varias películas.

---

## Instalación local

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd eva1
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

```bash
# Windows PowerShell
venv\Scripts\Activate.ps1

# Linux / macOS
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

> Si `mysqlclient` falla en Windows, instala primero el conector de MySQL o usa PyMySQL como alternativa (ver comentario en requirements.txt).

### 5. Crear el archivo .env

```bash
# Copia el archivo de ejemplo
copy .env.example .env   # Windows
cp .env.example .env     # Linux/macOS
```

Edita `.env` con tus valores reales (ver sección Variables de entorno).

### 6. Crear la base de datos en MySQL

```sql
CREATE DATABASE eva2_portal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'eva2_user'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON eva2_portal.* TO 'eva2_user'@'localhost';
FLUSH PRIVILEGES;
```

### 7. Ejecutar migraciones

```bash
python manage.py migrate
```

### 8. Importar datos iniciales desde JSON

```bash
python manage.py importar_datos
```

Este comando lee los archivos `static/data/*.json` y crea los registros en la base de datos sin duplicados.

### 9. Crear superusuario para Django Admin

```bash
python manage.py createsuperuser
```

### 10. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

Accede en: [http://localhost:8000](http://localhost:8000)
Django Admin en: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## Variables de entorno

El archivo `.env` debe estar en la misma carpeta que `manage.py` y **nunca** debe subirse al repositorio.

```env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=eva2_portal
DB_USER=eva2_user
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

El archivo `.env.example` contiene la estructura sin valores reales y sí se incluye en el repositorio como referencia.

---

## Base de datos

El proyecto usa MySQL/MariaDB con codificación `utf8mb4`.

**Diagrama de relaciones:**

```
Genero ←── Juego ──→ Plataforma
             (FK)      (M2M)

Director ←── Pelicula
               (FK)

Estreno (independiente)
```

- `Juego.genero` → ForeignKey a `Genero` (SET_NULL si se elimina el género)
- `Juego.plataformas` → ManyToManyField con `Plataforma`
- `Pelicula.director` → ForeignKey a `Director` (SET_NULL si se elimina el director)

---

## Django Admin

El CRUD completo de todos los modelos se realiza desde `/admin/`.

| App | Modelos disponibles |
|---|---|
| app_games | Género, Plataforma, Juego |
| app_movies | Director, Película, Estreno |

Cada modelo incluye:
- `list_display` para ver columnas relevantes en el listado
- `search_fields` para búsqueda por texto
- `list_filter` para filtros laterales
- `filter_horizontal` en Juego para gestionar plataformas (ManyToMany)

---

## Flujo de datos

```
Base de datos (MySQL)
       ↓
Django Models (ORM)
       ↓
Views (select_related / prefetch_related)
       ↓
Templates (Bootstrap 5)
       ↓
Navegador
```

Los archivos JSON en `static/data/` se conservan únicamente como fuente de importación inicial. Las vistas **no** los leen; consultan exclusivamente la base de datos.

---

## Comandos útiles

```bash
# Verificar configuración del proyecto
python manage.py check

# Ver estado de migraciones
python manage.py showmigrations

# Importar datos desde JSON (solo la primera vez o para actualizar)
python manage.py importar_datos

# Iniciar servidor local
python manage.py runserver
```
