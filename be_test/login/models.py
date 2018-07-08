from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from .validators import UsernameValidator

# Create your models here.


# ------------
# 用户主表
# 自定义validator
# ------------
class UserMain(AbstractUser):
    username_validator = UsernameValidator()

