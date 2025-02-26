from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import serializers

from .models import User, Tasks
from .services import TaskService


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'is_staff',
            'is_superuser'
        )

class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Simple register Serializer
    """
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        """
        Override the hash password via 'create_user() method'
        :param validated_data:
        :return:
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

class UserLoginSerializer(serializers.Serializer):
    """
    Simple Login Session based for testing.
    """
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError("Invalid credentials, try again")
            if not user.is_active:
                raise serializers.ValidationError("Account disabled, contact admin")
            attrs['user'] = user
        else:
            raise serializers.ValidationError("Both username and password are required")
        return attrs

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

    def validate(self, data):
        instance = self.instance
        new_status = data.get('status', instance.status if instance else None)

        # Block user to change from completed to started
        if instance and instance.status == Tasks.StatusChoices.COMPLETED:
            if new_status != Tasks.StatusChoices.COMPLETED:
                raise serializers.ValidationError(
                    "Completed tasks cannot be modified"
                )
        return data

    def update(self, instance, validated_data):
        return TaskService.update_task(instance, validated_data)

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
