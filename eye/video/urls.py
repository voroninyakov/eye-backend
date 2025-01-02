from django.urls import path

from .views import VideoListCreateView, CommentListCreateView, VideoRetrieveDestroyView, ReactionCreateView, \
    ReactionRetrieveUpdateDestroyView, CommentRetrieveUpdateDestroyView, VideoViewCreateView

app_name = 'video'

urlpatterns = [
    path('video/', VideoListCreateView.as_view()),
    path('video/<int:pk>/', VideoRetrieveDestroyView.as_view(), name='detail'),
    path('video/<int:video_pk>/comments/', CommentListCreateView.as_view(), name='comments'),
    path('video/<int:video_pk>/comments/<pk>', CommentRetrieveUpdateDestroyView.as_view(), name='comment_detail'),
    path('video/<int:video_pk>/reactions/', ReactionCreateView.as_view(), name='reactions'),
    path('video/<int:video_pk>/reactions/<pk>', ReactionRetrieveUpdateDestroyView.as_view(), name='reaction_detail'),
    path('video/<int:video_pk>/view', VideoViewCreateView.as_view(), name='video_view'),
]
