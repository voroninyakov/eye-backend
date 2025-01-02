from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Video, Comment, Reaction, VideoView
from account.models import Profile
from .serializers import VideoSerializer, CommentSerializer, ReactionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class VideoListCreateView(generics.ListCreateAPIView):
    queryset = Video.published.all()
    serializer_class = VideoSerializer

    def perform_create(self, serializer):
        profile = get_object_or_404(Profile, user=self.request.user)
        serializer.save(author=profile)


class VideoRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.published.all()

    def destroy(self, request, *args, **kwargs):
        profile = get_object_or_404(Profile, user=self.request.user)
        self.queryset = Video.objects.filter(author=profile)
        return super().destroy(request, *args, **kwargs)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Video.objects.get(pk=self.kwargs.get('video_pk')).comments.all()

    def perform_create(self, serializer):
        video = get_object_or_404(Video, pk=self.kwargs['video_pk'])
        serializer.save(author=self.request.user, video=video)


class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Video.objects.get(pk=self.kwargs['video_pk']).comments

class ReactionCreateView(generics.CreateAPIView):
    serializer_class = ReactionSerializer

    def perform_create(self, serializer):
        video = get_object_or_404(Video, pk=self.kwargs['video_pk'])
        try:
            Reaction.objects.get(video=video, author=self.request.user)
        except Reaction.DoesNotExist:
            serializer.save(author=self.request.user, video=video)


class ReactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReactionSerializer

    def get_queryset(self):
        return Video.objects.get(pk=self.kwargs['video_pk']).reactions

class VideoViewCreateView(APIView):
    def post(self, request, *args, **kwargs):
        video = get_object_or_404(Video, pk=self.kwargs['video_pk'])
        try:
            VideoView.objects.get(video=video, author=self.request.user)
            return Response({'status': 'alredy'})
        except VideoView.DoesNotExist:
            new_model = VideoView(video=video, author=self.request.user)
            new_model.save()
            return Response({'status': 'success'})