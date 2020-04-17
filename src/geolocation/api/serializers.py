from rest_framework import serializers
from ..models import Location, ReceptionCenter, Region


class LocationSerializer(serializers.ModelSerializer):
    """
    Location Serializer.
    """
    class Meta:
        model = Location
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
