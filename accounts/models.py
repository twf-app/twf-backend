from django.contrib.auth.models import AbstractUser
from django.db import models
from geoposition.fields import GeopositionField
from phonenumber_field.modelfields import PhoneNumberField


class Member(AbstractUser):
    """
    Create Member class.
    """
    phone = PhoneNumberField()
    image = models.ImageField(upload_to='user', null=True)
    default_location = GeopositionField(null=False)
    show_profile = models.BooleanField(default=True)
    show_check_ins = models.BooleanField(default=True)
    show_events = models.BooleanField(default=True)
    show_images = models.BooleanField(default=True)
    show_contact_method = models.BooleanField(default=True)

    def settings_options(self):
        if self.show_profile is False:
            pass
        else:
            pass

        if self.show_check_ins is False:
            pass
        else:
            pass





    def latest_location(self):
        last_location = self.check_ins.latest('place')
        return last_location

    def __str__(self):
        return str(self.username)
