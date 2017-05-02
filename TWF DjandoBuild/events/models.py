from django.db import models
from datetime import datetime


# Create your models here.


class Journey(models.Model):
    name = models.CharField(max_length=15)
    member = models.ManyToManyField('accounts.Member', related_name='members')
    # check_in = models.DateTimeField()
    zone = models.ManyToManyField('places.Zone', related_name='zones', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class CheckIn(models.Model):
    member = models.ForeignKey('accounts.Member', on_delete=models.CASCADE, related_name='check_ins')
    journey = models.ForeignKey('events.Journey', related_name='checked_into', null=True, blank=True)
    time = models.DateTimeField(null=False)
    location = models.ForeignKey('places.Location', related_name='check_ins', blank=True, null=False)
    zone = models.ForeignKey('places.Zone') #TODO; Fix Zones so that multi-users can be checked in to same Zone.
    geotag = models.ManyToManyField('places.GeoTag', related_name='geotags', blank=True)

    def timestamp(self):
        self.check_in = datetime.now()

    def __str__(self):
        return f"{self.member.username} is Checked-In to {self.zone.location}  @  {self.time} !"

    class Meta:
        ordering = ('-time',)

