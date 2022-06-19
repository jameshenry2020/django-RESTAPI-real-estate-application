import logging

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.profiles.models import Profile

User = settings.AUTH_USER_MODEL

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    logger.info(f"{instance}'s profile created")
