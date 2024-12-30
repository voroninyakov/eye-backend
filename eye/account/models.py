from django.db.models import ImageField
from django.contrib.auth.models import AbstractUser
from .utils import user_avatar_upload_path


class EUser(AbstractUser):
    avatar = ImageField(upload_to=user_avatar_upload_path, blank=True)
