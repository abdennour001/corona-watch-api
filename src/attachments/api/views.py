from rest_framework import generics
from ..models import Attachment
from .serializers import AttachmentSerializer


class AttachmentListView(generics.ListAPIView):
    """
    get:
    Return list of all attachments.
    """
    lookup_field = 'id'
    serializer_class = AttachmentSerializer

    def get_queryset(self):
        queryset = Attachment.objects.all()
        return queryset
