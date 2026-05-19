from django.db import models
from users.models import User
from teams.models import Team

class Task(models.Model):

    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=255)

    description = models.TextField()

    deadline = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    assigned_users = models.ManyToManyField(
        User,
        related_name='tasks'
    )

    created_at = models.DateTimeField(auto_now_add=True)