from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import user_avatar_upload_path, profile_cover_upload_path


class EUser(AbstractUser):
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(to=EUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    bio = models.CharField(blank=True, max_length=500)
    cover = models.ImageField(upload_to=profile_cover_upload_path, blank=True)
    followers = models.ForeignKey(to="EUser", on_delete=models.CASCADE, related_name='follows')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
