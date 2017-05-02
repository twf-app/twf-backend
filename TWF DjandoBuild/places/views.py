from django.shortcuts import render
from rest_framework import viewsets
from places.serializers import LocationSerializer, ZoneSerializer, GeotagSerializer
from places.models import Zone, Location, GeoTag


# Create your views here.


class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all().order_by('-created_time')
    serializer_class = LocationSerializer


class ZoneViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer


class GeotagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = GeoTag.objects.all()
    serializer_class = GeotagSerializer
