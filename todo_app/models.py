import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Use the Django AbstractUser for compatibility
    """
    def __str__(self):
        return self.username

    def __repr__(self):
        return (f"User(first_name={repr(self.first_name)},"
                f" date_joined={repr(self.date_joined)},"
                f" is_active={repr(self.is_active)},"
                f" date_joined={repr(self.date_joined)},"
                f" last_login={repr(self.last_login)},"
                f" email={repr(self.email)})")
    pass

class Tasks(models.Model):
    class StatusChoices(models.TextChoices):
        COMPLETED = 'Completed'
        STARTED = 'Started'
        CREATED = 'Created'

    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_user')
    created_at = models.DateTimeField(auto_now_add=True)
    started_at = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    duration = models.DateTimeField(null=True, blank=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices, # type: ignore
        default=StatusChoices.CREATED)

    def __str__(self):
        return f"Task {self.task_id} by {self.user.username}"

    def __repr__(self):
        return (f"Tasks(task_id={repr(self.task_id)},"
                f" user_id={repr(self.user.id)},"
                f" user_name={repr(self.user.username)},"
                f" created_at={repr(self.created_at)},"
                f" status={repr(self.status)} )")