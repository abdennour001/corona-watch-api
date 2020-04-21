from rest_framework import generics
from ..models import SuspectedCase, Declared
from .serializers import SuspectedCaseSerializer, SuspectedCaseUpdateSerializer, DeclaredSerializer, DeclaredUpdateSerializer


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


class SuspectedCaseRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
    get:
    Get the suspected case with ( pk="id" ).

    delete:
    Delete the suspected case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseSerializer
    queryset = SuspectedCase.objects.all()


class SuspectedCaseUpdateView(generics.UpdateAPIView):
    """
    put:
    Update the suspected case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = SuspectedCaseUpdateSerializer
    queryset = SuspectedCase.objects.all()


class DeclaredCreateListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all Declared that exists.

    post:
    Report a new Declared case in the system.
    """
    lookup_field = 'id'
    serializer_class = DeclaredSerializer
    queryset = Declared.objects.all()


class DeclaredRetrieveDeleteView(generics.RetrieveDestroyAPIView):
    """
    get:
    Get the Declared case with ( pk="id" ).

    delete:
    Delete the Declared case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = DeclaredSerializer
    queryset = Declared.objects.all()


class DeclaredUpdateView(generics.UpdateAPIView):
    """
    put:
    Update the Declared case with ( pk="id" ).
    """
    lookup_field = 'id'
    serializer_class = DeclaredUpdateSerializer
    queryset = Declared.objects.all()
