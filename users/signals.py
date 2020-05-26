from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile, CustomUser, Stats

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=CustomUser)
def create_user_stats(sender, instance, created, **kwargs):
    if created:
        Stats.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_stats(sender, instance, **kwargs):
    instance.stats.save()