from django.urls import path
from .views import YoutubeSearch

urlpatterns = [
    path("youtube/", YoutubeSearch.as_view(), name="youtube-search")
]
