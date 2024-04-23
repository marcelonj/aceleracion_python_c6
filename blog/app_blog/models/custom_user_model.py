from django.contrib.auth.models import User
from django.db import models


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    fecha_nac = models.DateField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
