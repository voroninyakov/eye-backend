from django.db import models
from account.models import Profile, EUser
from django.contrib.postgres.fields import DateTimeRangeField
from .utils import video_file_upload_path, video_cover_upload_path


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    file = models.FileField(upload_to=video_file_upload_path)
    cover = models.ImageField(upload_to=video_cover_upload_path)
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('a', 'Archived'),
    )
    status = models.CharField(choices=STATUS, default='d', max_length=1)


class VideoView(models.Model):
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE)
    author = models.ForeignKey(to=EUser, on_delete=models.CASCADE)
    view_time = DateTimeRangeField()

class Comment(models.Model):
    author = models.ForeignKey(to=EUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=3000)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

class Reaction(models.Model):
    like = models.BooleanField(default=True)
    author = models.ForeignKey(to=EUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE)
