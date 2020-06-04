from rest_framework import generics, views, status
from rest_framework.response import Response
from django.db.models import Q
from .serializers import YoutubeVideoSerializer, YoutubeVideo
from django.shortcuts import Http404


class YoutubeVideosList(generics.ListAPIView):
    """
        get:
        Return a list of all existing videos.
    """
    lookup_field = 'id'
    serializer_class = YoutubeVideoSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = YoutubeVideo.objects.all()
        query = self.request.GET.get('validated')
        if query is not None:
            queryset = queryset.filter(
                is_validated__exact=True if query in ['true', 'yes', '1'] else False if query in ['false', 'no', '0'] else False
            ).distinct()
        return queryset


class ValidateYoutubeVideo(views.APIView):
    """
    Validate a youtube video
    """

    @staticmethod
    def get_video(video_id):
        try:
            video = YoutubeVideo.objects.get(pk=video_id)
        except YoutubeVideo.DoesNotExist:
            raise Http404
        return video

    def put(self, request, video_id):
        video = self.get_video(video_id)
        video.is_validated = not video.is_validated
        video.save()
        return Response(status=status.HTTP_201_CREATED)
