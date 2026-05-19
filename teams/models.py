from django.db import models
from users.models import User

class Team(models.Model):

    name = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)


class TeamMember(models.Model):

    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )