from django.db import models


class CheckIn(models.Model):
    """Model to allow users to 'check-in': say that they are in a place."""

    member = models.ForeignKey('accounts.Member', on_delete=models.CASCADE, related_name='check_ins')
    journey = models.ForeignKey('journeys.Journey', related_name='checked_into', null=True, blank=True)
    time = models.DateTimeField(null=False, auto_now=True)

    tags = models.ManyToManyField('activities.Tag')

    #TODO: Geolocation implementation...
    # location = models.ForeignKey('places.Location', related_name='check_ins', blank=True, null=False)
    # zone = models.ForeignKey('places.Zone') #TODO; Fix Zones so that multi-users can be checked in to same Zone.
    # geotag = models.ManyToManyField('places.GeoTag', related_name='geotags', blank=True)


class Review(models.Model):
    """A Review for a business that someone goes to. May need to link into Yelp, Places, etc."""

    # Meat of the review
    business_name = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024)
    body = models.TextField()
    stars = models.SmallIntegerField()

    # Associated Models
    tags = models.ManyToManyField('activities.Tag', related_name='tag_review')
    check_in = models.ForeignKey('activities.CheckIn')
    member = models.ForeignKey('accounts.Member')

    # Will the review be shared on external sites?
    share_yelp = models.BooleanField(default=False)
    share_google = models.BooleanField(default=False)
    share_foursquare = models.BooleanField(default=False)


class JournalEntry(models.Model):
    """An entry in a user's travel journal that is associated with a specific journey they are on."""

    # Association with member, journey and time
    member = models.ForeignKey('accounts.Member', related_name='member_journal_entry')
    journey = models.ForeignKey('journeys.Journey', related_name='journey_journal_entry')
    time = models.DateTimeField(null=False, auto_now=True)

    # Meat of the JournalEntry
    #TODO: Need picture uploading?
    title = models.CharField(max_length=1024)
    body = models.TextField()
    tags = models.ManyToManyField('activities.Tag', related_name='tag_journal_entry')


class Tag(models.Model):
    """A way for a member to organize or show off their content. Will be generated by company and members."""

    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024)