from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    travel_preferences = models.JSONField(default=dict)
    past_trips = models.JSONField(default=list)
    wishlist_destinations = models.JSONField(default=list)
    
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related name to avoid conflict
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Custom related name to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )