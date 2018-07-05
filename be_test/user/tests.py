from django.test import TestCase
from user.models import User, Profile


def create_user(username, password=None, email=None, last_ip='127.0.0.1'):
    """
    A helper function to create a user.

    :param username: Username
    :param password: Password
    :param email: Email
    :param last_ip: IP address of last login
    :return: A new profile associated with the newly-created user.
    """
    user = User.objects.create_user(username, email, password)
    profile = Profile.objects.create(user_id=user.id, last_ip=last_ip)
    user.save()
    profile.save()
    return profile


class UserTestCase(TestCase):
    def setUp(self):
        self.john = create_user('john', 'thisisjohnspw', 'john@example.org')
        self.jack = create_user('jack', 'iamafool', 'jack@instance.com', '192.168.23.33')

    def test_email(self):
        self.assertEqual('john@example.org', self.john.user.email)
        self.assertEqual('jack@instance.com', self.jack.user.email)

    def test_last_ip(self):
        self.assertEqual('127.0.0.1', self.john.last_ip)
        self.assertEqual('192.168.23.33', self.jack.last_ip)
