from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Additional information to a User object:
    - IP address of last login (or null)
    - IP address of last logout (or null)
    - Date and time of last logout (or null)
    """
    user = models.OneToOneField(User, models.CASCADE)
    last_logout = models.DateTimeField(null=True)
    last_login_ip = models.GenericIPAddressField(null=True)
    last_logout_ip = models.GenericIPAddressField(null=True)


USERNAME_MAX = User._meta.get_field('username').max_length
PASSWORD_MAX = User._meta.get_field('password').max_length
