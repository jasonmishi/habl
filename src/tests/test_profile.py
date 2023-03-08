import pytest

from accounts.models import Profile, User


@pytest.mark.django_db
def test_profile_create():
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    assert User.objects.count() == 1
    profile = Profile.objects.get(user=user)
    assert profile.email == user.email


@pytest.mark.django_db
def test_profile_edit():
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    profile = Profile.objects.get(user=user)

    profile.email = "new@mail.com"
    user.refresh_from_db()

    assert profile.email == user.email


@pytest.mark.django_db
def test_profile_premium():
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    profile = Profile.objects.get(user=user)

    assert profile.is_premium() is False

    user.make_premium()

    assert profile.is_premium() is True
