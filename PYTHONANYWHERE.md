# PythonAnywhere Deployment

## Project files already prepared

- `requirements.txt`
- `faenas/webplayground/webplayground/wsgi.py`
- `faenas/webplayground/webplayground/settings.py`
- `.env.example`

## What to configure on PythonAnywhere

1. Create a new virtualenv with Python 3.13.
2. Install dependencies:
   `pip install -r /home/your_user/faenas/requirements.txt`
3. Set these environment variables:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `EMAIL_HOST`
   - `EMAIL_HOST_USER`
   - `EMAIL_HOST_PASSWORD`
   - `EMAIL_PORT`
   - `EMAIL_USE_TLS=True`
4. Point the WSGI file to `faenas/webplayground/webplayground/wsgi.py`.
5. Set the project directory to `/home/your_user/faenas/faenas/webplayground`.
6. Run migrations:
   `python manage.py migrate`
7. Collect static files:
   `python manage.py collectstatic`
8. Make sure the web app domain includes `agsatpc.com` and `www.agsatpc.com`.

## Notes

- The project is already compatible with Python 3.13 in this workspace.
- `django-ckeditor` still shows a security warning because it bundles CKEditor 4.