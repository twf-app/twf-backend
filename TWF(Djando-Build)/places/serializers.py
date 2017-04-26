from places.models import Location, Zone, GeoTag
from rest_framework import serializers


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('position', 'created_time')


class ZoneSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model = Zone
        fields = ('geotag', 'location', 'radius_meters')


class GeotagSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoTag
        fields = ('name',)
