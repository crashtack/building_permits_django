# http://eli.thegreenplace.net/2014/02/15/programmatically-populating-a-django-database
from django.core.management.base import BaseCommand
from django.db import IntegrityError
import json
from maps.models import Permit
from math import floor


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_permit(self):
        """Add permits to database from JSON data"""
        # Reading data back
        # file_path = 'media/contruction.json'
        file_path = 'curb.json'
        with open(file_path, 'r') as f:
            data = json.load(f)

        count = 0
        for perm in data:
            # permit = Permit(
            #     permit_number=perm['application_permit_number'],
            #     latitude=perm['latitude'],
            #     longitude=perm['longitude'],
            # )
            if perm.get('final_date') is None:
                print("#: {}".format(perm['application_permit_number']))
                print('lat: {}'.format(perm['latitude']))
                print('lng: {}\n'.format(perm['longitude']))
        #     # permit.save()
                count += 1
        print('Count: {}'.format(count))
        # for key in data[0].keys():
            # print(key)

    def _save_permit_to_database(self):
        """Add a permit to the database"""
        file_path = 'media/contruction.json'
        with open(file_path, 'r') as f:
            data = json.load(f)

        count = 0
        for perm in data:
            if perm.get('final_date') is None and perm.get('latitude') and perm.get('longitude'):

                if perm.get('description'):
                    if len(perm.get('description')) >= 255:
                        perm['description'] = perm.get('description')[0:255]

                permit = Permit(
                    permit_number=perm['application_permit_number'],
                    latitude=perm['latitude'],
                    longitude=perm['longitude'],
                    master_use_permit=perm.get('master_use_permit'),
                    action_type=perm.get('action_type'),
                    address=perm.get('address'),
                    applicant_name=perm.get('applicant_name'),
                    application_date=perm.get('application_date'),
                    issue_date=perm.get('issue_date'),
                    final_date=perm.get('final_date'),
                    experation_date=perm.get('experation_date'),
                    category=perm.get('category'),
                    description=perm.get('description'),
                    url=perm.get('permit_and_complaint_status_url'),
                    permit_type=perm.get('permit_type'),
                    status=perm.get('status'),
                    value=int(perm.get('value')),
                    work_type=perm.get('work_type'),
                    contractor=perm.get('contractor'),
                )
                try:
                    # print("Adding permit to DB: {}".format(perm))
                    permit.save()
                    # print()
                except IntegrityError:
                    # print("Premit {} is already in the database".format(perm.get('application_permit_number')))
                    pass

                count += 1

        print('count: {}'.format(count))
                # if count > 2:
                #     return

    def _list_permits():
        pass

    def _hello(self):
        """ Say Hello """
        print('hello\n')

    def handle(self, *args, **options):
        self._hello()
        # self._create_permit()
        self._save_permit_to_database()
