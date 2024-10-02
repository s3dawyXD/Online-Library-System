#!/bin/bash

# Apply database migrations
echo "Applying database migrations..."
python online_library_system/manage.py migrate


# Start Django app
echo "Starting Django application..."
python online_library_system/manage.py runserver 0.0.0.0:8000 &

# Keep the container running
wait
