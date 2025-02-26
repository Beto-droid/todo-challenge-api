# import pytest
# from todo_app.serializers import UserRegistrationSerializer, TasksUpdateSerializer
#
# @pytest.mark.django_db
# def test_user_registration_serializer():
#     data = {'username': 'serializeruser', 'password': 'testpass'}
#     serializer = UserRegistrationSerializer(data=data)
#     assert serializer.is_valid()
#     user = serializer.save()
#     assert user.check_password('testpass')
#
# @pytest.mark.django_db
# def test_task_update_serializer(test_task):
#     data = {'status': 'Completed'}
#     serializer = TasksUpdateSerializer(instance=test_task, data=data)
#     assert not serializer.is_valid()  # Should fail because task isn't started