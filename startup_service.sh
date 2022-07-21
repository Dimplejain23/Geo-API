#!/bin/bash
# Start GEOAPI 
echo "Starting GEOAPI"
./wait-for-it.sh postgres:5432 -- echo "DB started"
python geoapp/manage.py makemigrations countries_app
python geoapp/manage.py migrate
cd /code/geoapp
gunicorn 'geoapp.wsgi' \
    --bind 0.0.0.0:$PORT \
    --workers 2 \
    --threads=2 \
    --daemon \
    --worker-connections=1000 \
    --preload -c /code/gunicorn_config.py \
    --access-logfile "/var/log/geoapi.log" \
    --error-logfile "/var/log/geoapi_error.log"

tail -f /dev/null