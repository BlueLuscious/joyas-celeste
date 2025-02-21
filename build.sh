#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install Locale es_AR.UTF-8
apt-get update
apt-get install -y locales
locale-gen es_AR.UTF-8
update-locale LANG=es_AR.UTF-8

# Upgrade PIP
pip install --upgrade pip

# Install Requirements
pip install -r requirements.txt

# Move to App
cd app

# Collect Static Files
python manage.py collectstatic --no-input

# Migrate
python manage.py migrate

# Create Superuser
python manage.py createfirstuser
