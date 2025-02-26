from django.utils import timezone
from django.db import transaction

from todo_app.models import Tasks


class TaskService:
    @staticmethod
    @transaction.atomic
    def update_task(instance, validated_data):
        """
        Main entry point for task updates
        Returns updated task instance
        """
        new_status = validated_data.get('status', instance.status)

        if new_status != instance.status:
            instance = TaskService._handle_status_change(instance, new_status)

        for attr, value in validated_data.items():
            if attr != 'status':
                setattr(instance, attr, value)

        instance.save()
        return instance

    @staticmethod
    def _handle_status_change(instance, new_status):
        if new_status == Tasks.StatusChoices.STARTED:
            if not instance.started_at:
                instance.started_at = timezone.now()
            instance.completed_at = None
            instance.duration = None

        elif new_status == Tasks.StatusChoices.COMPLETED:
            if not instance.started_at:
                raise ValueError("Cannot complete unstarted task")
            instance.completed_at = timezone.now()
            instance.duration = instance.completed_at - instance.started_at

        elif new_status == Tasks.StatusChoices.CREATED:
            instance.started_at = None
            instance.completed_at = None
            instance.duration = None

        instance.status = new_status
        return instance