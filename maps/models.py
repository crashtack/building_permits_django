from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


class Permit(models.Model):
    """
    A Model for the permit data.
    """
    permit_number = models.IntegerField('Permit Number')
    master_use_permit = models.IntegerField('Master Use Permit', blank=True)
    action_type = models.CharField('Action Type', max_length=24, blank=True)
    address = models.CharField('Address', max_length=50, blank=True)
    applicant_name = models.CharField('Applicant Name', max_length=24, blank=True)
    application_date = models.DateTimeField('Application Date', blank=True)
    issue_date = models.DateTimeField('Issue Date', blank=True)
    final_date = models.DateTimeField('Final Date', blank=True)
    experation_date = models.DateTimeField('Experation Date', blank=True)
    category = models.CharField('Category', max_length=24, blank=True)
    description = models.CharField('Description', max_length=255, blank=True)
    latitude = models.FloatField('Latitude', blank=True)
    longitude = models.FloatField('Longitude', blank=True)
    url = models.URLField('URL', blank=True)
    permit_type = models.CharField('Type', max_length=24, blank=True)
    status = models.CharField('Status', max_length=24, blank=True)
    value = models.IntegerField('Value', blank=True)
    work_type = models.CharField('Work Type', max_length=24, blank=True)
    contractor = models.CharField('Contractor', max_length=55, blank=True)
