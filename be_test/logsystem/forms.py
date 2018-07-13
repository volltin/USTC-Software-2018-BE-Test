# -*- coding: utf8 -*- #
from django import forms
from .models import *
from django.core.exceptions import ValidationError
from .models import User
import re
class RegisterForm(forms.Form):
    username=forms.CharField(min_length=1,max_length=256,required=True,error_messages={"required":"The username cannot be empty",
                                                                                       "min_length":"The username required at least 1 character",
                                                                                       "max_length":"The username is not allowed more than 256 characters"})
    password=forms.CharField(min_length=6,max_length=20,required=True,error_messages={"required":"The password cannot be empty",
                                                                                      "min_length":"The password required at least 6 character",
                                                                                      "max_length":"The password is not allowed more than 20 characters"})


    def clean_username(self):
        username=self.cleaned_data.get('username')
        patten=re.compile(r'^[0-9a-zA-Z@\_]+$')        #用户名只能包含数字、字母、@\_

        if not patten.match(username):
            raise ValidationError(u'The username has invalid character!')
        else:
            pass
        users=User.objects.filter(username=username).count()

        if users:
            raise ValidationError(u'The user is already existed!')
        else:
            return username

    def clean_password(self):
        ret=self.cleaned_data.get("password")
        patten = re.compile(r'^[0-9a-zA-Z@\_~!#$%^&*()]+$')  # 密码可以包含的字符

        if not patten.match(ret):
            raise ValidationError(u'The password has invalid character!')
        else:
            pass
        return self.cleaned_data.get("password")

class LoginForm(forms.Form):
    username=forms.CharField(min_length=1,max_length=256,required=True,error_messages={"required":"The username cannot be empty",
                                                                                       "min_length":"The username required at least 1 character",
                                                                                       "max_length":"The username is not allowed more than 256 characters"})
    password=forms.CharField(min_length=6,max_length=20,required=True,error_messages={"required":"The password cannot be empty",
                                                                                      "min_length":"The password required at least 6 character",
                                                                                      "max_length":"The password is not allowed more than 20 characters"})

    def clean(self):
        username=self.cleaned_data.get('username')
        password=self.cleaned_data.get('password')
        user=User.objects.filter(username=username).first()
        if username and password:
            if not user:
                raise ValidationError("The user is not existed")
            elif password!=user.password:
                raise ValidationError("Wrong password")
            return self.cleaned_data.get('username')