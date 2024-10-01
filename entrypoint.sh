#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Run tests
echo "Running tests..."
pytest

# Start Django app
echo "Starting Django application..."
python manage.py runserver 0.0.0.0:8000 &

# Keep the container running
wait
