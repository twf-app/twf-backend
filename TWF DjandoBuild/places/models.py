from django.db import models
from geoposition.fields import GeopositionField


class Location(models.Model):
    position = GeopositionField()
    created_time = models.DateTimeField(auto_created=True)

    def __str__(self):
        return str(self.position)


class GeoTag(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Zone(models.Model):
    geotag = models.ManyToManyField('places.GeoTag', related_name='zones')
    location = models.ForeignKey(Location, null=False)
    radius_meters = models.PositiveSmallIntegerField(default=500, blank=True, null=False)

    def __str__(self):
        return str(self.location)
