from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from myapp.models import AnotherModel

@receiver(post_save, sender=User)
def user_saved(sender, instance, **kwargs):
        AnotherModel.objects.create(related_user=instance, description="In Transaction")
