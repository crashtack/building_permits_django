# http://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
from django.core.management.base import BaseCommand
import json
from maps.models import Permit


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    # def _create_tags(self):
    #     tlisp = Tag(name='Lisp')
    #     tlisp.save()
    #
    #     tjava = Tag(name='Java')
    #     tjava.save()

    def _create_permit(self):
        """Add permits to database from JSON data"""
        # Reading data back
        with open('curb.json', 'r') as f:
            data = json.load(f)

        for perm in data:
            permit = Permit(
                permit_number=perm['application_permit_number'],
                latitude=perm['latitude'],
                longitude=perm['longitude'],
            )
            print("#: {}".format(perm['application_permit_number']))
            print('lat: {}'.format(perm['latitude']))
            print('lng: {}\n'.format(perm['longitude']))
            permit.save()

    def _hello(self):
        """ Say Hello """
        print('hello\n')

    def handle(self, *args, **options):
        self._hello()
        self._create_permit()
