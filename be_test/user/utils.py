import re

USERNAME_PATTERN = re.compile('[_0-9a-zA-Z]+')
PASSWORD_PATTERN = re.compile('[~!@#$%^&*()_+`0-9-=a-zA-Z]+')


def is_well_formed_username(username):
    """
    Check if @username is well-formed, ie. only consists of alphabets, digits, and underscore.
    :param username: username to check
    :return: True if well-formed, False otherwise
    """
    return True if USERNAME_PATTERN.fullmatch(username) else False


def is_well_formed_password(password):
    """
    Check if @password is well-formed, ie. only consists of ~ ! @ # $ % ^ & * ( ) _ + ` digits
    alphabets.
    :param password: password to check
    :return: True if well-formed, False otherwise
    """
    return True if PASSWORD_PATTERN.fullmatch(password) else False


def is_secure_password(password):
    """
    Check if @password is strong enough, ie.
    1. have 5 characters or more

    Note: the criteria may change in the future.

    :param password: password to check
    :return: True if considered secure, False otherwise
    """
    return len(password) >= 5
