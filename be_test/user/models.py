from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Additional information to a User object:
    - IP address of last activity (register, login, or logout).
    """
    user = models.OneToOneField(User, models.CASCADE)
    last_ip = models.GenericIPAddressField()


USERNAME_MAX = User._meta.get_field('username').max_length
PASSWORD_MAX = User._meta.get_field('password').max_length
