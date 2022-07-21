from celery import Celery
from celery.schedules import crontab
import os
from celery import shared_task
from .helpers import ProcessData
from celery.schedules import crontab
  

# Create default Celery app
app = Celery('downloaderApp',
             backend='rpc://',
             broker=os.environ.get("BROKER_URL"))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'geoapp.geoapp.settings')

app.config_from_object("django.conf:settings", namespace="CELERY")

# Create a task to run in async to download and upload countries data
@shared_task(name='process_data')
def data_to_db_task():
    return ProcessData()

# Celery beat scheduler to trigger every 10 minutes
app.conf.beat_schedule = {
      'process-every-10-minutes': {
        'task': 'process_data',
        'schedule': crontab(minute='*/10'),
        'options': {
            'expires': 30.0,
        },
    },
} 