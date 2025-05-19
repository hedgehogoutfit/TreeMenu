#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Migrate database
python manage.py makemigrations
python manage.py migrate

# Load mock data
python manage.py load_mock_data

# Run server
python manage.py runserver