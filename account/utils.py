# your_app/utils.py
from datetime import datetime
from django.contrib.auth import get_user_model
from account.models import Notification, AssignTask, ApplyLeaves,Holiday,Feed

User = get_user_model()

def create_notification_functions():
    # 1. Birthday notifications
    today = datetime.now().date()
    users_with_birthday = User.objects.filter(date_of_birth__month=today.month, date_of_birth__day=today.day)

    for user in users_with_birthday:
        message = f"Happy Birthday, {user.full_name}!"
        Notification.objects.create(user=user, message=message)

    # 2. Task assignment notifications
    assigned_tasks = AssignTask.objects.filter(task_date=today)

    for task in assigned_tasks:
        message = f"Task assigned: {task.task_name} for {task.assignee_name}"
        Notification.objects.create(user=task.assignee_name, message=message)

    # 3. Pending task notifications
    pending_tasks = AssignTask.objects.filter(completion_status__lt='100%', task_date__lt=today)

    for task in pending_tasks:
        message = f"Pending task: {task.task_name} for {task.assignee_name}"
        Notification.objects.create(user=task.assignee_name, message=message)

    # 4. Leave application notifications
    pending_leave_applications = ApplyLeaves.objects.filter(admin_approve=False, tl_approve=False)

    for leave_app in pending_leave_applications:
        message = f"Leave application from {leave_app.name} - {leave_app.subject}"
        Notification.objects.create(user=leave_app.name, message=message)

    # 5. Leave approval and cancellation notifications
    approved_leave_applications = ApplyLeaves.objects.filter(admin_approve=True, tl_approve=True)

    for leave_app in approved_leave_applications:
        message = f"Leave approved: {leave_app.subject} for {leave_app.name}"
        Notification.objects.create(user=leave_app.name, message=message)

    canceled_leave_applications = ApplyLeaves.objects.filter(admin_cancel=True, tl_cancel=True)

    for leave_app in canceled_leave_applications:
        message = f"Leave canceled: {leave_app.subject} for {leave_app.name}"
        Notification.objects.create(user=leave_app.name, message=message)

    # 6. Holiday notifications
    holidays = Holiday.objects.filter(date=datetime.now().date())

    for holiday in holidays:
        message = f"Happy {holiday.holidayname}!"
        Notification.objects.create(user=User.objects.all(), message=message)

    # 7. Salary slip generation notifications
    # Assuming you have a model for salary slips and the logic for generating them
    # Adjust this logic based on your salary slip model and generation process

    # 8. Posting feeds notifications
    new_feeds = Feed.objects.filter(date=datetime.now().date())

    for feed in new_feeds:
        message = f"New feed posted: {feed.desc}"
        Notification.objects.create(user=User.objects.all(), message=message)

    # 9. Updating status of the API notifications
    # Assuming you have a model for API status and the logic for updating them
    # Adjust this logic based on your API status model and update process    
