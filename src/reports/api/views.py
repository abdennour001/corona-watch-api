from rest_framework import generics
from ..models import SuspectedCase
from .serializers import SuspectedCaseSerializer


class SuspectedCaseListView(generics.ListAPIView):
    """
    get:
    Return a list of all reports that exists.
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializer
    queryset = SuspectedCase.objects.all()


class ReportSuspectedCase(generics.CreateAPIView):
    """
    post:
    Report a new suspected case in the system.
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializer
    queryset = SuspectedCase.objects.all()

    def perform_create(self, serializer):
        pass


class SuspectedCaseRUDView(generics.RetrieveUpdateDestroyAPIView):
    pass
