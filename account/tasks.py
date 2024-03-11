from celery import shared_task
from django.utils import timezone
from .models import *

@shared_task
def check_overdue_tasks():
    overdue_tasks = AssignTask.objects.filter(due_date__lt=timezone.now(), overdue_duedate=False)
    for task in overdue_tasks:
        task.overdue_duedate = True
        task.save()

@shared_task
def delete_old_records():
    sixty_days_ago = timezone.now() - timezone.timedelta(days=60)
    old_records = EmployeeDetails.objects.filter(task_date__lt=sixty_days_ago)
    old_records.delete()