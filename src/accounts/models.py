from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    pass

    def make_premium(self):
        group, _ = Group.objects.get_or_create(name="premium")
        self.groups.add(group)


# Group.objects.get_or_create(name='premium')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    bio = models.TextField()

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
        instance.profile.save()
