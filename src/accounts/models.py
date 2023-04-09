from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    pass

    def make_premium(self):
        group, _ = Group.objects.get_or_create(name="premium")
        self.groups.add(group)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

    # properties and setters attributes from User model
    @property
    def first_name(self):
        return self.user.first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self.user.first_name = new_first_name
        self.user.save()

    @property
    def last_name(self):
        return self.user.last_name

    @last_name.setter
    def last_name(self, new_last_name):
        self.user.last_name = new_last_name
        self.user.save()

    @property
    def email(self):
        return self.user.email

    @email.setter
    def email(self, new_email):
        self.user.email = new_email
        self.user.save()

    def is_premium(self):
        return self.user.groups.filter(name="premium").exists()

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
