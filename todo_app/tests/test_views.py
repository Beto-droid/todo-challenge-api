import pytest
from django.urls import reverse
from rest_framework import status
from todo_app.models import Tasks

@pytest.mark.django_db
def test_registration(api_client):
    """
    Test registration session
    :param api_client:
    :return:
    """
    url = reverse('registration')
    data = {'username': 'newuser', 'password': 'newpass123'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_task_list_user_1_single_task(api_client, test_user_1, test_task_1_for_user_1):
    """
    Get the tasks for user 1, should be 1 task
    :param api_client:
    :param test_user_1:
    :param test_task_1_for_user_1:
    :return:
    """
    api_client.force_authenticate(user=test_user_1)
    url = reverse('tasks-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1

@pytest.mark.django_db
def test_task_list_user_2_double_task(api_client, test_user_2, test_tasks_for_user_2):
    """
    Get the tasks for user 2, should be 2 task
    :param api_client:
    :param test_user_2:
    :param test_tasks_for_user_2:
    :return:
    """
    api_client.force_authenticate(user=test_user_2)
    url = reverse('tasks-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 3

@pytest.mark.django_db
def test_update_task_user_2(api_client, test_user_2, test_tasks_for_user_2):
    """
    Test Update all fields of a task
    :param api_client:
    :param test_user_2:
    :param test_tasks_for_user_2:
    :return:
    """
    api_client.force_authenticate(user=test_user_2)
    updated_data = {
        'title': 'Updated Task Title',
        'description': 'Updated Description',
        'status': Tasks.StatusChoices.STARTED,
    }
    url = reverse('tasks-detail', args=[test_tasks_for_user_2[1].task_id])
    response = api_client.put(url, updated_data, format='json')
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == updated_data['title']
    assert response.data['description'] == updated_data['description']
    assert response.data['status'] == updated_data['status']

@pytest.mark.django_db
def test_update_user_2_status_completed_to_another_should_fail(api_client, test_user_2, test_tasks_for_user_2):
    """
    This test will update try to update a task that is already completed, it should not be able to.
    :param api_client:
    :param test_user_2:
    :param test_tasks_for_user_2:
    :return:
    """
    api_client.force_authenticate(user=test_user_2)
    updated_data = {
        'status': Tasks.StatusChoices.STARTED,
    }
    url = reverse('tasks-detail', args=[test_tasks_for_user_2[2].task_id])
    response = api_client.patch(url, updated_data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {
        'task_status': ['Completed tasks cannot be modified']
    }


@pytest.mark.django_db
def test_delete_task_user_2(api_client, test_user_2, test_tasks_for_user_2):
    """
    Test Delete Task
    :param api_client:
    :param test_user_2:
    :param test_tasks_for_user_2:
    :return:
    """
    api_client.force_authenticate(user=test_user_2)
    url = reverse('tasks-detail', args=[test_tasks_for_user_2[1].task_id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert response.status_code == status.HTTP_204_NO_CONTENT
    url = reverse('tasks-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2

@pytest.mark.django_db
def test_admin_user_list(admin_client):
    url = reverse('user-list')
    response = admin_client.get(url)
    assert response.status_code == status.HTTP_200_OK