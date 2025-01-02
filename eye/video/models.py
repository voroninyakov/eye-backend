from django.db import models
from account.models import Profile, EUser
from django.urls import reverse

from .utils import video_file_upload_path, video_cover_upload_path

class VideoPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='p')


# Create your models here.
class Video(models.Model):
    objects = models.Manager()
    published = VideoPublishedManager()
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    file = models.FileField(upload_to=video_file_upload_path)
    cover = models.ImageField(upload_to=video_cover_upload_path)
    author = models.ForeignKey(to=Profile, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True, editable=False)
    STATUS = (
        ('d', 'Draft'),
        ('p', 'Published'),
        ('a', 'Archived'),
    )
    status = models.CharField(choices=STATUS, default='d', max_length=30)

    def url(self):
        return reverse('video:detail', kwargs={'pk': self.pk})

class VideoView(models.Model):
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE)
    author = models.ForeignKey(to=EUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    author = models.ForeignKey(to=EUser, on_delete=models.CASCADE, editable=False)
    text = models.CharField(max_length=3000)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE, related_name='comments')

class Reaction(models.Model):
    like = models.BooleanField(default=True)
    author = models.ForeignKey(to=EUser, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(to=Video, on_delete=models.CASCADE, related_name='reactions')


    class Meta:
        unique_together = ('author', 'video')
