from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Birthplace(models.Model):
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=40)

class Stats(models.Model):
    tasks_completed = models.IntegerField()
    tasks_ongoing = models.IntegerField()
    tasks_abandoned = models.IntegerField()
    tasks_total = models.IntegerField()
    tasks_archived = models.IntegerField()

class UserProfile(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    profile_picture = models.ImageField()
    about_me = models.TextField()
    birth_place = models.ForeignKey(
        Birthplace,
        on_delete=models.CASCADE
    )
    stats = models.ForeignKey(
        Stats,
        on_delete=models.CASCADE
    )