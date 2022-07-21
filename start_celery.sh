#!/bin/bash
# Start Celery 
echo "Starting Celery"
celery -A geoapp.countries_app.celery beat -l info --logfile=/var/log/celery.beat.log --detach
celery -A geoapp.countries_app.celery worker -l info --logfile=/var/log/celery.log 