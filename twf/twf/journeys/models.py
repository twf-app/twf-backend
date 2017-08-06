from django.db import models


class Journey(models.Model):
    """
    Compendium of all actions for a member on a trip.
    Includes:
        CheckIns
        JournalEntries
        Associated Reviews
        Associated Pictures
        
    Will be used for making pre-made websites of a member's activity as well as tracking user progress(best wording?).
    """
    member = models.ManyToManyField('accounts.Member', related_name='members')
    
    name = models.CharField(max_length=1024)
    description = models.TextField()
    
    check_ins = models.DateTimeField()
    
    # zone = models.ManyToManyField('places.Zone', related_name='zones', blank=True) Not using zones anymore?

    def __str__(self):
        return self.name