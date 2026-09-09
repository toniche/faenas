# Faenas / AGSatPC

Proyecto Django para el sitio de AGSatPC.

## Requisitos

- Python 3.13.
- Variables de entorno:
  - `DJANGO_SECRET_KEY`
  - `DJANGO_DEBUG`
  - `EMAIL_HOST_PASSWORD`
  - `EMAIL_HOST`
  - `EMAIL_HOST_USER`
  - `EMAIL_PORT`
  - `EMAIL_USE_TLS`

## Desarrollo local

1. Crear y activar el entorno nuevo:
	`python3.13 -m venv .venv313`
	`source .venv313/bin/activate`
2. Instalar dependencias:
	`pip install -r requirements.txt`
3. Ejecutar comprobación:
	`cd faenas/webplayground`
	`python manage.py check`

## Subir a GitHub

1. Asegúrate de no incluir secretos ni entornos virtuales en el commit.
2. Revisa el estado con `git status`.
3. Haz commit de los cambios útiles:
	`git add README.md requirements.txt faenas/requirements.txt faenas/webplayground/webplayground/settings.py faenas/webplayground/faenas/urls.py faenas/webplayground/messenger/models.py faenas/webplayground/messenger/views.py .gitignore`
4. Sube el repositorio al remoto de GitHub.

## Producción en PythonAnywhere

1. Crear un virtualenv nuevo con Python 3.13 en PythonAnywhere.
2. Instalar dependencias con `pip install -r /home/tu_usuario/faenas/requirements.txt`.
3. Configurar las variables de entorno en la pestaña Web o en el bash config de PythonAnywhere:
	- `DJANGO_SECRET_KEY`
	- `DJANGO_DEBUG=False`
	- `EMAIL_HOST_PASSWORD`
	- `EMAIL_HOST`, `EMAIL_HOST_USER`, `EMAIL_PORT`, `EMAIL_USE_TLS`
4. Apuntar el WSGI a `faenas/webplayground/webplayground/wsgi.py`.
5. En el archivo de configuración de la web, usar como directorio del proyecto `/home/tu_usuario/faenas/faenas/webplayground`.
6. Ejecutar migraciones:
	`python manage.py migrate`
7. Recopilar estáticos:
	`python manage.py collectstatic`
8. Verificar que `ALLOWED_HOSTS` incluya `agsatpc.com` y `www.agsatpc.com`.
9. Configurar el dominio para que `www.agsatpc.com` y `agsatpc.com` apunten al mismo sitio.

## Estado actual

- `python manage.py check` pasa en el entorno `faenas/.venv313`.
- Queda una advertencia de `django-ckeditor` por CKEditor 4, que conviene reemplazar antes de producción si quieres eliminar riesgos de seguridad.