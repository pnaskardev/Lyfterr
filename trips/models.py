from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import reverse

import uuid

from django.conf import settings

class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'

    # Add a unique related_name for the groups field
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    # Add a unique related_name for the user_permissions field
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Trip(models.Model):
    REQUESTED = 'requested'
    STARTED = 'started'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'
    STATUSES = (
        (REQUESTED, 'Requested'),
        (STARTED, 'Started'),
        (IN_PROGRESS, 'In progress'),
        (COMPLETED, 'Completed'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    pick_up_address=models.CharField(max_length=255)
    drop_off_address=models.CharField(max_length=255)
    status=models.CharField(max_length=20,choices=STATUSES,default=REQUESTED)
    
    driver=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_driver'
    )

    rider=models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name='trips_as_rider'
    )

    def __str__(self):
        return f'{self.id}'
    
    def get_absolute_url(self):
        return reverse('trip:trip_detail',kwargs={'trip_id':self.id})