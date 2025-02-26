import pytest
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
def test_jwt_obtain_correct_user(api_client, test_user_1):
    url = reverse('token_obtain_pair')
    response = api_client.post(url, {
        'username': test_user_1.username,
        'password': 'testpass123'
    })
    assert response.status_code == 200
    assert 'access' in response.data

@pytest.mark.django_db
def test_jwt_refresh(api_client, test_user_1):
    refresh = RefreshToken.for_user(test_user_1)
    url = reverse('token_refresh')
    response = api_client.post(url, {'refresh': str(refresh)})
    assert response.status_code == 200
    assert 'access' in response.data

@pytest.mark.django_db
def test_jwt_obtain_wrong_password(api_client, test_user_1):
    url = reverse('token_obtain_pair')
    response = api_client.post(url, {
        'username': test_user_1.username,
        'password': 'WrongPassword'
    })
    assert response.status_code == 401
    assert 'detail' in response.data
    assert response.data['detail'].code == 'no_active_account'