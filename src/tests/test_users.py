import pytest

from accounts.models import Profile, User


@pytest.mark.django_db
def test_user_create():
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    assert User.objects.count() == 1
    assert Profile.objects.count() == 1
    assert user.profile.email == "lennon@thebeatles.com"
