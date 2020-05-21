web: gunicorn proyecto.wsgi --log-file -
release: python manage.py makemigrations --no-input && python manage.py migrate --no-input