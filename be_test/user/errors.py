"""
User Error Definition (100~199)
"""
from be_test.errors import *

INVALID_CREDS = {'err_code': 100, 'err_msg': 'Invalid credentials'}
USER_EXISTS = {'err_code': 101, 'err_msg': 'This username is already taken'}
USER_NOT_EXISTS = {'err_code': 102, 'err_msg': "This user doesn't exist"}
USERNAME_TOO_LONG = {'err_code': 110, 'err_msg': 'This username is too long'}
PASSWORD_TOO_LONG = {'err_code': 111, 'err_msg': 'This password is too long'}
PASSWORD_TOO_SIMPLE = {'err_code': 112, 'err_msg': 'This password is too simple'}
ILLEGAL_USERNAME = {'err_code': 113, 'err_msg': 'This username contains illegal characters'}
ILLEGAL_PASSWORD = {'err_code': 114, 'err_msg': 'This password contains illegal characters'}
