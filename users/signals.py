from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# creating a profile eveytime a user is created
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwags):
    if created:
        Profile.objects.create(user=instance)

# saves our profile everytime user object gets saved
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwags):
    instance.profile.save()
