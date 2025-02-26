# import pytest
# from django.utils import timezone
# from todo_app.models import Tasks
#
# @pytest.mark.django_db
# def test_task_creation(test_user):
#     task = Tasks.objects.create(
#         user=test_user,
#         title='New Task',
#         description='Description'
#     )
#     assert task.status == Tasks.StatusChoices.CREATED
#
# @pytest.mark.django_db
# def test_status_transition(test_task):
#     test_task.status = Tasks.StatusChoices.STARTED
#     test_task.save()
#     assert test_task.started_at is not None
#
#     test_task.status = Tasks.StatusChoices.COMPLETED
#     test_task.save()
#     assert test_task.completed_at is not None
#     assert isinstance(test_task.duration, timezone.timedelta)