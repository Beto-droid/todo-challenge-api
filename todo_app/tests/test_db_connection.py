import pytest

@pytest.mark.django_db
def test_database_connection():
    assert True