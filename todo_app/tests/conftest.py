import pytest
from rest_framework.test import APIClient

from todo_app.models import Tasks, User
import logging

@pytest.fixture(autouse=True)
def disable_logging():
    logging.disable(logging.CRITICAL)
    logging.disable(logging.WARNING)

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user_1():
    return User.objects.create_user(
        username='testuser1',
        password='testpass123',
    )

@pytest.fixture
def test_task_1_for_user_1(test_user_1):
    return Tasks.objects.create(
        user=test_user_1,
        title='Test Task 1 for user 1',
        description='Test Description 1 for user 1',
        status=Tasks.StatusChoices.CREATED
    )

@pytest.fixture
def test_user_2():
    return User.objects.create_user(
        username='testuser2',
        password='testpass123',
    )

@pytest.fixture
def test_tasks_for_user_2(test_user_2):
    task_1 = Tasks.objects.create(
        user=test_user_2,
        title='Test Task 1 for user 2',
        description='Test Description 1 for user 2',
        status=Tasks.StatusChoices.CREATED
    )
    task_2 = Tasks.objects.create(
        user=test_user_2,
        title='Test Task 2 for user 2',
        description='Test Description 2 for user 2',
        status=Tasks.StatusChoices.CREATED
    )
    task_3 = Tasks.objects.create(
        user=test_user_2,
        title='Test Task 2 for user 2',
        description='Test Description 2 for user 2',
        status=Tasks.StatusChoices.COMPLETED
    )
    return task_1, task_2, task_3

@pytest.fixture
def admin_client():
    admin = User.objects.create_superuser(
        username='admintest',
        password='adminpass',
    )
    client = APIClient()
    client.force_authenticate(user=admin)
    return client