from rest_framework import serializers
from ..models import Location, ReceptionCenter, Region, State, Town


class LocationSerializer(serializers.ModelSerializer):
    """
    Location Serializer.
    """
    class Meta:
        model = Location
        fields = '__all__'


class TownSerializer(serializers.ModelSerializer):
    """
    Town Serializer.
    """

    location = LocationSerializer(read_only=True)

    class Meta:
        model = Town
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    """
    State Serializer.
    """

    class Meta:
        model = State
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = Region
        fields = '__all__'


class ReceptionCenterSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = ReceptionCenter
        fields = '__all__'
