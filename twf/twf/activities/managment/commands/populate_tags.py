# python imports
import pandas as pd

# django imports
from django.core.management.base import BaseCommand

# module level imports
from activities.models import Tag
from twf.settings import LOCAL_PATH


class Command(BaseCommand):
    """Command to populate the database with all spells for 5th Edition."""

    # args
    help = 'Will auto populate the database with predefined tags for members to use.'

    def handle(self, *args, **kwargs):

        with open(LOCAL_PATH + 'data/twf-data-tables') as f:
            tags = pd.read_csv(f, delimiter=',')

        tags = tags.dropna()

        for tag in tags.iterrows():

            Tag.objects.create(
                name=tag[1][0],
                description=tag[1][1],
            )
