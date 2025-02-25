import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


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

    # This will update the started and completed fields.
    def save(self, *args, **kwargs):
        match self.status:
            # This is the normal. the user passed from created to started to completed.
            case self.StatusChoices.STARTED:
                self.started_at = timezone.now()
            case self.StatusChoices.COMPLETED:
                time_now = self.completed_at  # Mini perf, 1 call
                self.completed_at = time_now
                self.task_duration = self.started_at - time_now
            case _:
                pass

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Task {self.task_id} by {self.user.username}"

    def __repr__(self):
        return (f"Tasks(task_id={repr(self.task_id)},"
                f" user_id={repr(self.user.id)},"
                f" user_name={repr(self.user.username)},"
                f" created_at={repr(self.created_at)},"
                f" status={repr(self.status)} )")