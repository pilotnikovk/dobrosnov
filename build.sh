#!/bin/bash
# Build script for Railway

echo "Running collectstatic..."
python manage.py collectstatic --no-input

echo "Running migrations..."
python manage.py migrate --no-input

echo "Creating superuser (if needed)..."
python manage.py initadmin

echo "Build completed!"
