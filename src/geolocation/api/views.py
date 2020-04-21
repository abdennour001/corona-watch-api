from rest_framework import generics
from ..models import Location, Region, ReceptionCenter, State, Town
from .serializers import LocationSerializer, RegionSerializer, ReceptionCenterSerializer, StateSerializer, TownSerializer
from django.db.models import Q


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

    def get_queryset(self):
        valid_bool = {
            'true': [True],
            'false': [False],
            None: [True, False]
        }
        queryset = Town.objects.all()
        query_is_risked = self.request.GET.get('risked')
        query_is_validated = self.request.GET.get('validated')
        if query_is_risked or query_is_validated is not None:
            queryset = queryset.filter(
                Q(is_risked__in=valid_bool[query_is_risked]),
                Q(is_validated__in=valid_bool[query_is_validated])
            ).distinct()
        return queryset


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


class StateTownList(generics.ListAPIView):
    """
    get:
    Get the list of towns of the state with ( pk="state_id" ).
    """
    lookup_field = 'id'
    serializer_class = TownSerializer

    def get_queryset(self):
        queryset = Town.objects.filter(state=self.kwargs.get('state_id'))
        return queryset
