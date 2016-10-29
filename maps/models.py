from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings


class Permit(models.Model):
    """
    A Model for the permit data.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             related_name='permits',
                             related_query_name='permits')
    permit_number = models.IntegerField('Permit Number', unique=True)
    master_use_permit = models.IntegerField('Master Use Permit', blank=True, null=True)
    action_type = models.CharField('Action Type', max_length=25, blank=True, null=True)
    address = models.CharField('Address', max_length=50, blank=True, null=True)
    applicant_name = models.CharField('Applicant Name', max_length=24, blank=True, null=True)

    date_created = models.DateField('Date Created', auto_now_add=True)
    date_modified = models.DateField('Date Modified', auto_now=True)
    application_date = models.DateTimeField('Application Date', blank=True, null=True)
    issue_date = models.DateTimeField('Issue Date', blank=True, null=True)
    final_date = models.DateTimeField('Final Date', blank=True, null=True)
    experation_date = models.DateTimeField('Experation Date', blank=True, null=True)

    category = models.CharField('Category', max_length=24, blank=True, null=True)
    description = models.CharField('Description', max_length=255, blank=True, null=True)
    latitude = models.FloatField('Latitude', blank=True)
    longitude = models.FloatField('Longitude', blank=True)
    url = models.URLField('URL', blank=True, null=True)
    permit_type = models.CharField('Type', max_length=24, blank=True, null=True)
    status = models.CharField('Status', max_length=32, blank=True, null=True)
    value = models.IntegerField('Value', blank=True, null=True)
    work_type = models.CharField('Work Type', max_length=24, blank=True, null=True)
    contractor = models.CharField('Contractor', max_length=55, blank=True, null=True)

    def __unicode__(self):
        return ''.format(self.permit_number)

    def __str__(self):
        return ''.format(self.permit_number)

    class Meta:
        ordering = ('application_date',)


class List(models.Model):
    """
    A list of Permit
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             blank=True,
                             null=True,
                             related_name='list',
                             related_query_name='list')
    permits = models.ManyToManyField('Permit',
                                     related_name='list',
                                     blank=True,
                                     )
    title = models.CharField('Title', name='title', max_length=24)
