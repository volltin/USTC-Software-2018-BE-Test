from django.db import models

# Create your models here.

class Users(models.Model):
    '''
    用户表的 ORM 映射。
    '''
    name = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=50)
    login_time = models.IntegerField(default=24)
    update_date = models.DateTimeField(auto_now=True)
    update_ip = models.GenericIPAddressField(null=True,blank=True)



