from rest_framework import serializers

from .models import User, Tasks


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_staff',
            'is_superuser'
        )


class TasksSerializer(serializers.ModelSerializer):
    tasks_id = serializers.UUIDField(read_only=True)
    # These are read_only, bc if not the user can edit them.
    created_at = serializers.DateTimeField(read_only=True)
    started_at = serializers.DateTimeField(read_only=True)
    completed_at = serializers.DateTimeField(read_only=True)
    task_duration = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tasks
        fields = (
            'tasks_id',
            'user',
            'status',
            'tasks_description',
            'created_at',
            'started_at',
            'completed_at',
            'task_duration',
        )