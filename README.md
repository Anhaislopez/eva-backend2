# Portal Geek & Dev — EVA2

## Descripción

Portal web desarrollado con Django que integra dos módulos principales:

- **Videojuegos**: catálogo de juegos indie con géneros y plataformas.
- **Películas y Estrenos**: cartelera geek y próximos estrenos con recomendaciones.

La aplicación utiliza una base de datos relacional (MySQL) gestionada mediante Django ORM.
El CRUD completo se administra desde Django Admin.

---

## URLs del proyecto desplegado

| Recurso | URL |
|---|---|
| Aplicación | http://44.216.250.23:8000 |
| Django Admin | http://44.216.250.23:8000/admin/ |
| phpMyAdmin | http://44.216.250.23/phpmyadmin |

**Credenciales Django Admin:** usuario `admin` / contraseña `admin1234`

---

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python 3.14 | Lenguaje principal |
| Django 5.2 | Framework web |
| MySQL | Base de datos relacional |
| Django ORM | Consultas a la base de datos |
| Django Admin | CRUD de todos los modelos |
| Bootstrap 5 | Estilos y componentes UI |
| python-dotenv | Variables de entorno |
| Git / GitHub | Control de versiones |
| AWS EC2 | Servidor en la nube |

---

## Aplicaciones

### app_games

Gestiona el catálogo de videojuegos.

**Modelos:**
- `Genero` — nombre único. Un género puede agrupar varios juegos.
- `Plataforma` — nombre único. Una plataforma puede tener varios juegos.
- `Juego` — título, género (ForeignKey), plataformas (ManyToManyField), descripción e imagen.

**Relaciones:**
- `Juego → Genero`: ForeignKey, varios juegos pueden compartir el mismo género.
- `Juego ↔ Plataforma`: ManyToManyField, un juego puede estar en varias plataformas y viceversa.

### app_movies

Gestiona la cartelera y los próximos estrenos.

**Modelos:**
- `Director` — nombre único.
- `Pelicula` — título, director (ForeignKey), año e imagen.
- `Estreno` — título, fecha, recomendación e imagen.

**Relaciones:**
- `Pelicula → Director`: ForeignKey, un director puede tener varias películas.

---

## Acceso SSH a EC2 (desde cualquier PC)

### Requisitos previos
- Tener el archivo `ubuntu.pem` (clave SSH de la instancia)
- Tener Git instalado
- **Windows:** usar PowerShell o Git Bash

### Conectarse a la instancia

```powershell
# Windows PowerShell
ssh -i "ruta\a\ubuntu.pem" ubuntu@44.216.250.23
```


> Si da error de permisos en Windows, ejecutar primero:
> ```powershell
> icacls "ruta\a\ubuntu.pem" /inheritance:r /grant:r "$($env:USERNAME):(R)"
> ```

> En Linux/macOS:
> ```bash
> chmod 400 ubuntu.pem
> ```

---

## Encender el servidor Django en EC2

Una vez conectado por SSH:

```bash
# 1. Ir al proyecto
cd ~/eva-backend2/eva1

# 2. Activar el entorno virtual
source venv/bin/activate

# 3. Iniciar el servidor
python manage.py runserver 0.0.0.0:8000
```

El servidor queda disponible en: **http://44.216.250.23:8000**

Para detenerlo: `Ctrl + C`

---

## Instalación desde cero en EC2 (si se clona en una instancia nueva)

```bash
# 1. Clonar el repositorio
git clone https://github.com/Anhaislopez/eva-backend2.git
cd eva-backend2/eva1

# 2. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear el archivo .env (ver sección Variables de entorno)
nano .env

# 5. Ejecutar migraciones
python manage.py migrate

# 6. Importar datos iniciales desde JSON
python manage.py importar_datos

# 7. Crear superusuario para Django Admin
python manage.py createsuperuser

# 8. Iniciar servidor
python manage.py runserver 0.0.0.0:8000
```

---

## Instalación local (en tu PC)

```bash
# 1. Clonar el repositorio
git clone https://github.com/Anhaislopez/eva-backend2.git
cd eva-backend2/eva1

# 2. Crear y activar entorno virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Crear .env desde el ejemplo
copy .env.example .env   # Windows
cp .env.example .env     # Linux/macOS

# 5. Editar .env con tus credenciales locales
# 6. Crear la base de datos MySQL local
# 7. Ejecutar migraciones
python manage.py migrate

# 8. Importar datos
python manage.py importar_datos

# 9. Crear superusuario
python manage.py createsuperuser

# 10. Iniciar servidor
python manage.py runserver
```

---

## Variables de entorno

El archivo `.env` debe estar en la misma carpeta que `manage.py`.
**Nunca subir `.env` al repositorio** (está en `.gitignore`).

```env
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=44.216.250.23,localhost,127.0.0.1

DB_NAME=eva2_portal
DB_USER=eva2_user
DB_PASSWORD=tu_password
DB_HOST=localhost
DB_PORT=3306
```

Usa `.env.example` como referencia (incluido en el repositorio sin contraseñas reales).

---

## Base de datos

El proyecto usa MySQL con codificación `utf8mb4`.

**Diagrama de relaciones:**

```
Genero ←── Juego ──→ Plataforma
             (FK)      (M2M)

Director ←── Pelicula
               (FK)

Estreno (independiente)
```

Crear la base en MySQL:

```sql
CREATE DATABASE eva2_portal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'eva2_user'@'localhost' IDENTIFIED BY 'tu_password';
GRANT ALL PRIVILEGES ON eva2_portal.* TO 'eva2_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## Django Admin

El CRUD completo se realiza desde `/admin/`.

| App | Modelos |
|---|---|
| app_games | Género, Plataforma, Juego |
| app_movies | Director, Película, Estreno |

Cada modelo tiene `list_display`, `search_fields`, `list_filter`.
Juego usa `filter_horizontal` para gestionar plataformas (ManyToMany).

---

## Comandos útiles

```bash
# Verificar configuración
python manage.py check

# Ver migraciones aplicadas
python manage.py showmigrations

# Importar datos desde JSON
python manage.py importar_datos

# Servidor local
python manage.py runserver

# Servidor accesible desde exterior
python manage.py runserver 0.0.0.0:8000
```

---

## Repositorio

https://github.com/Anhaislopez/eva-backend2

---

## Credenciales del proyecto (solo para revisión académica)

### Servidor EC2
| Parámetro | Valor |
|---|---|
| IP Elástica | 44.216.250.23 |
| Usuario SSH | ubuntu |
| Clave SSH | ubuntu.pem |

### Django Admin
| Parámetro | Valor |
|---|---|
| URL | http://44.216.250.23:8000/admin/ |
| Usuario | admin |
| Contraseña | admin1234 |

### phpMyAdmin
| Parámetro | Valor |
|---|---|
| URL | http://44.216.250.23/phpmyadmin |
| Usuario | eva2_user |
| Contraseña | Eva2_Pass2026! |
| Base de datos | eva2_portal |

### MySQL (conexión directa)
| Parámetro | Valor |
|---|---|
| Host | localhost |
| Puerto | 3306 |
| Base de datos | eva2_portal |
| Usuario | eva2_user |
| Contraseña | Eva2_Pass2026! |
