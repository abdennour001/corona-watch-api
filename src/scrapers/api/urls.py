from django.urls import path
from .views import YoutubeVideosList, ValidateYoutubeVideo

urlpatterns = [
    path("youtube/", YoutubeVideosList.as_view(), name="youtube-list"),
    path("youtube/validate/<video_id>", ValidateYoutubeVideo.as_view(), name="youtube-validate-video")
]
