from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    last_log_in_time = models.DateTimeField('last log in time')
    last_log_out_time = models.DateTimeField('last log out time')
    last_log_in_IP = models.GenericIPAddressField('last log in IP')
    last_log_out_IP = models.GenericIPAddressField ('last log out IP')
