from rest_framework import serializers
from .models import Video, Comment, Reaction, VideoView

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text', 'author', 'upload_date']

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['url', 'title', 'description', 'file', 'cover', 'author', 'status', 'upload_date']


class ReactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reaction
        fields = ['like', 'time']
