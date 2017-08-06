from django.db import models
from django.contrib.auth.models import AbstractUser


class Member(AbstractUser):
    """
    Creates the Member class. Will need to be able to track everything associated with a member.
    
    From AbstractUser we have:
        username
        password
        first_name
        last_name
        email
        is_staff - Admin access
        is_active
        date_joined
    """

    # Additional Member Information:
    phone_number = models.IntegerField(null=True, blank=True)  # TODO: Get better phone number validation information.
    # home_location = GeopositionField(null=False)
    profile_picture = models.ImageField(upload_to='user', null=True)
    
    # Account Information:
    premium_member = models.BooleanField(default=False)

    # Profile Settings:
    show_profile = models.BooleanField(default=True)
    show_check_ins = models.BooleanField(default=True)
    # show_events = models.BooleanField(default=True) Using this?
    show_images = models.BooleanField(default=True)
    show_contact_method = models.BooleanField(default=True)

    def settings_options(self):
        if self.show_profile:
            """Allow other users to see profile information."""

        if self.show_check_ins:
            """Allow other users to see where the member has been."""

        if self.show_images:
            """Allow other users to see member uploaded images."""

        if self.show_contact_method:
            """Make the contact method public for member."""

    def latest_location(self):
        last_location = self.check_ins.latest('place')
        return last_location

    def __str__(self):
        return self.username

