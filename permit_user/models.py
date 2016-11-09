from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.dispatch import receiver
from django.db.models.signals import post_save
import uuid
from django.contrib.auth.models import User
from django.conf import settings


@receiver(post_save, sender=User)
def make_sure_user_profile_is_added_on_user_created(sender, **kwargs):
    """
    Creates a PermitUser when a User:user is created
    """
    if kwargs.get('created', False):
        up = PermitUser.objects.create(user=kwargs.get('instance'))


class PermitUserProfileManager(models.Manager):
    """
    Returns a queryset pre-filtered to active profiles
    """
    class Meta:
        model = "PermitUser"

    def get_queryset(self):
        """
        Returns a queryset of active users
        """
        return User.objects.filter(is_active=True)


@python_2_unicode_compatible
class PermitUser(models.Model):
    """
    The Permit User Model
    """
    user_uuid = models.UUIDField(primary_key=True,
                                 default=uuid.uuid4,
                                 editable=False,
                                 )
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name='permituser',)
    bio = models.CharField('Bio',
                           max_length=1024,
                           blank=True)
    latitude = models.FloatField('Latitude', blank=True, null=True)
    longitude = models.FloatField('Longitude', blank=True, null=True)
    location = models.CharField('Location',
                                max_length=128,
                                blank=True,
                                null=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

    objects = models.Manager()
    active = PermitUserProfileManager()
