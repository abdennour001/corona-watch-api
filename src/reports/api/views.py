from rest_framework import generics
from ..models import SuspectedCase
from .serializers import SuspectedCaseSerializer


class SuspectedCaseCreateListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all reports that exists.

    post:
    Report a new suspected case in the system.
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializer
    queryset = SuspectedCase.objects.all()


class SuspectedCaseRUDView(generics.RetrieveUpdateDestroyAPIView):
    pass
