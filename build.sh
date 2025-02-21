#!/usr/bin/env bash
# Exit on error
set -o errexit

# Move to App
cd app

# Upgrade PIP
pip install --upgrade pip

# Install Requirements
pip install -r requirements.txt

# Collect Static Files
python manage.py collectstatic --no-input

# Migrate
python manage.py migrate

# Create Superuser
python manage.py createfirstuser
