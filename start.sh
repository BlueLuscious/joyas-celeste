# Move to App
cd app

# Start App - Gunicorn
gunicorn app.wsgi --workers=3 --timeout=120
