release: python manage.py migrate && python manage.py collectstatic --noinput
web: gunicorn -w 4 mainProject.wsgi:application