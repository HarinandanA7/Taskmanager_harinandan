from django.core.mail import send_mail
from django.conf import settings

def send_task_email(to_email, task_title):

    subject = "New Task Assigned"

    message = f"You have been assigned a task: {task_title}"

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )