from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from django.shortcuts import get_object_or_404

class ProfileRetrieveView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class FollowView(APIView):
    def post(self, request, **kwargs):
        try:
            profile = get_object_or_404(Profile, id=kwargs.get('pk'))
            user = request.user
            if profile.followers.filter(id=user.id).exists():
                profile.followers.remove(user)
                return Response({'status': 'success', 'result': 'unfollow'})
            else:
                profile.followers.add(user)
                return Response({'status': 'success', 'result': 'follow'})
        except Exception as e:
            return Response({'status': 'error', 'detail': str(e)})
