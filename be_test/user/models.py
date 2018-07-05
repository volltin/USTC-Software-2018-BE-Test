from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Additional information to a User object:
    - IP address of last login.
    """
    user = models.OneToOneField(User, models.CASCADE)
    last_ip = models.GenericIPAddressField()

