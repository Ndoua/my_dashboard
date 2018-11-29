web: gunicorn dashboard.wsgi --log-file -
web: python dashboard/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT dashboard/settings.py
