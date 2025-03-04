# Move to App
cd app

# Start App - Gunicorn
gunicorn --bind :8000 app.wsgi:application
