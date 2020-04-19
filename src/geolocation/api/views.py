from rest_framework import generics
from ..models import Location, Region, ReceptionCenter, State, Town
from .serializers import LocationSerializer, RegionSerializer, ReceptionCenterSerializer, StateSerializer, TownSerializer


class LocationList(generics.ListAPIView):
    """
    get:
    Return a list of all locations.
    """
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationRetrieve(generics.RetrieveAPIView):
    """
    get:
    Return the specific Location ( pk='id' )
    """
    lookup_field = 'id'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class RegionListCreate(generics.ListCreateAPIView):
    """
    get:
    Return the region with ( pk='id' )
    post:
    Create a new region.
    """
    lookup_field = 'id'
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class RegionRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return region with ( pk='id' ).
    put:
    Update the region with ( pk='id' ).

    delete:
    Delete the region with ( pk='id' ).

    """
    lookup_field = 'id'
    serializer_class = RegionSerializer
    queryset = Region.objects.all()


class ReceptionCenterListCreate(generics.ListCreateAPIView):
    """
    get:
    Return the reception center with ( pk='id' ).

    post:
    Create a new reception center.

    """
    lookup_field = 'id'
    serializer_class = ReceptionCenterSerializer
    queryset = ReceptionCenter.objects.all()


class ReceptionCenterRUD(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Return the reception center with ( pk='id' ).

    put:
    Update the reception center with ( pk='id' ).

    delete:
    Delete the reception center with ( pk='id' ).

    """
    lookup_field = 'id'
    serializer_class = ReceptionCenterSerializer
    queryset = ReceptionCenter.objects.all()


class TownList(generics.ListAPIView):
    """
    get:
    Return list  of all towns.
    """
    lookup_field = 'id'
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class TownRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """
    get:
    Return the town with ( pk='id' ).

    put:
    Update the town with ( pk='id' ).
    """
    lookup_field = 'id'
    serializer_class = TownSerializer
    queryset = Town.objects.all()


class StateList(generics.ListAPIView):
    """
    get:
    Return list  of all States ( Wilayas ).
    """
    lookup_field = 'id'
    serializer_class = StateSerializer
    queryset = State.objects.all()


class StateRetrieve(generics.RetrieveAPIView):
    """
    get:
    Return the list with ( pk='id' ).
    """
    lookup_field = 'id'
    serializer_class = StateSerializer
    queryset = State.objects.all()
