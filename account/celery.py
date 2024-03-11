from celery import Celery
from celery.schedules import crontab

app = Celery('login_hola9')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'check-overdue-tasks-every-day': {
        'task': 'account.tasks.check_overdue_tasks',
        'schedule': crontab(minute=0, hour=0),  # Runs every day at midnight
    },
}




app = Celery('login_hola9')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-old-records-every-day': {
        'task': 'account.tasks.delete_old_records',
        'schedule': crontab(minute=0, hour=0),  # Runs every day at midnight
    },
}