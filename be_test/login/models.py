from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.


# ------------
# 用户主表
# 没有新增属性
# ------------
class UserMain(AbstractUser):
    pass

