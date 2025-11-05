from django.db.models.signals import post_save
from django.dispatch import receiver
from student.models import Profile
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_profile_user(sender, instance, created, **kwargs):
    """ this function create profile for users """
    if created:
        # create Profile
        Profile.objects.create(
            bio = f"{instance.firstname} bio",
            user=instance
        )