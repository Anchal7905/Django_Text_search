#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be available..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "PostgreSQL is up!"

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Start Django development server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
