import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'investpro.settings')

app = Celery('investpro')

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

app.conf.beat_schedule = {
    'price-update':{
        'task':'investEazyApp.tasks.compute_portfolio_data',
        'schedule':15,
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')