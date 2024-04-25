from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import CustomUser


@receiver(post_delete, sender=CustomUser)
def delete_user_on_customuser_delete(sender, instance, **kwargs):
    if instance.user and not instance._is_deleting:
        instance._is_deleting = True
        instance.user.delete()  # Eliminamos el usuario de Django


@receiver(post_delete, sender=User)
def delete_customuser_on_user_delete(sender, instance, **kwargs):
    if hasattr(instance, "customuser") and not instance.customuser._is_deleting:
        instance.customuser._is_deleting = True
        instance.customuser.delete()
