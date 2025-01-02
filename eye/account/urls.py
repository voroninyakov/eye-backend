from django.urls import path
from .views import ProfileListView, ProfileRetrieveView, FollowView

app_name = 'account'

urlpatterns = [
    path('', ProfileListView.as_view()),
    path('<int:pk>/', ProfileRetrieveView.as_view(), name='detail'),
    path('<int:pk>/follow/', FollowView.as_view(), name='follow'),
]
