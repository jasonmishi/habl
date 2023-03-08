import pytest

from accounts.models import User


@pytest.mark.django_db
def test_user_create():
    User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    assert User.objects.count() == 1
