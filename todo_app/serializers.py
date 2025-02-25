from django.db import transaction
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
    # These are read_only, bc if not the user can edit them.
    task_id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    started_at = serializers.DateTimeField(read_only=True)
    completed_at = serializers.DateTimeField(read_only=True)
    duration = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Tasks
        fields = (
            'task_id',
            'user',
            'status',
            'title',
            'description',
            'created_at',
            'started_at',
            'completed_at',
            'duration',
        )

class TasksCreateSerializer(serializers.ModelSerializer):
    # These are read_only, bc if not the user can edit them.
    task_id = serializers.UUIDField(read_only=True)

    def create(self, validated_data):
        with transaction.atomic():
            tasks = Tasks.objects.create(**validated_data)

            return tasks

    class Meta:
        model = Tasks
        fields = (
            'user',
            'task_id',
            'title',
            'description',
        )
        extra_kwargs = {
            'user': {'read_only': True}
        }

class TasksUpdateSerializer(serializers.ModelSerializer):
    task_id = serializers.UUIDField(read_only=True)

    def update(self, instance, validated_data):
        # orderitem_data = validated_data  # Maybe later add group ?

        with transaction.atomic():  # this lets us: if it fails, for example creating or deleting or whatever, it will rollback
            instance = super().update(instance, validated_data)  # This will update the Task Itself, not the child

        return instance

    class Meta:
        model = Tasks
        fields = (
            'user',
            'task_id',
            'title',
            'description',
            'status',
        )
        extra_kwargs = {
            'user': {'read_only': True}
        }
