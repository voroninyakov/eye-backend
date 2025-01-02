from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from .utils import user_avatar_upload_path, profile_cover_upload_path


class EUser(AbstractUser):
    avatar = models.ImageField(upload_to=user_avatar_upload_path, blank=True)

class Follow(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(to="Profile", on_delete=models.CASCADE)
    euser = models.ForeignKey(to=EUser, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(to=EUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    bio = models.CharField(blank=True, max_length=500)
    cover = models.ImageField(upload_to=profile_cover_upload_path, blank=True)
    followers = models.ManyToManyField(to="EUser", through=Follow, related_name='follows')

    def __str__(self):
        return self.name

    def url(self):
        return reverse("account:detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
