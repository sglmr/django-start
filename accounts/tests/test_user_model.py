import pytest
from django.contrib.auth import get_user_model

from accounts.models import User


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    ...


def test_simple_create_user():
    assert User.objects.count() == 0
    User.objects.create(name="john doe", email="john@example.com")
    assert User.objects.count() == 1


def test_correct_get_user_model():
    user_model = get_user_model()
    assert user_model == User
