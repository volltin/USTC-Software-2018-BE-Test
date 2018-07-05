import json
from django.test import Client, TestCase
from user.models import User, Profile
from user import errors


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


def decode(response):
    """
    Convert a JSONResponse to a dict.
    :param response: A JsonResponse object
    :return: A corresponding dict.
    """
    return json.loads(response.content.decode(response.charset))


class UserTestCase(TestCase):
    def setUp(self):
        self.good_password = 'He-lLo2333!'
        self.john = create_user('john', 'thisisjohnspw', 'john@example.org')
        self.jack = create_user('jack', 'iamafool', 'jack@instance.com', '192.168.23.33')

    def test_email(self):
        self.assertEqual('john@example.org', self.john.user.email)
        self.assertEqual('jack@instance.com', self.jack.user.email)

    def test_last_ip(self):
        self.assertEqual('127.0.0.1', self.john.last_ip)
        self.assertEqual('192.168.23.33', self.jack.last_ip)

    def test_register_insufficient_arguments(self):
        c = Client()
        rep1 = c.post('/user/register')
        rep2 = c.post('/user/register', {'username': 'hello'})
        rep3 = c.post('/user/register', {'password': 'hello-world'})
        self.assertEqual(rep1.status_code, 200)
        self.assertEqual(rep2.status_code, 200)
        self.assertEqual(rep3.status_code, 200)
        self.assertContains(rep1, "Insufficient arguments")
        self.assertContains(rep2, "Insufficient arguments")
        self.assertContains(rep3, "Insufficient arguments")

    def test_register_username_too_long(self):
        c = Client()
        rep = c.post('/user/register', {'username': 'a'*1000, 'password': 'He-lLo-123'})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, '110')
        self.assertContains(rep, "This username is too long")

    def test_register_illegal_username(self):
        c = Client()
        rep = c.post('/user/register', {'username': '?????????', 'password': 'He-lLo-123'})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, "This username contains illegal characters")

    def test_register_password_too_long(self):
        c = Client()
        rep = c.get('/user/register', {'username': 'hello', 'password': 'He-lLo-123'*1000})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, 'This password is too long')

    def test_register_illegal_password(self):
        c = Client()
        rep = c.get('/user/register', {'username': 'hello', 'password': 'Hello，你好, 早晨, こんにちは, 안녕하세요'})
        self.assertEqual(rep.status_code, 200)
        self.assertContains(rep, "This password contains illegal characters")

    def test_register_simple_password(self):
        c = Client()
        rep = c.get('/user/register', {'username': 'hello', 'password': '1'})
        self.assertContains(rep, 'This password is too simple')

    def test_register_logged_in(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspw'})
        self.assertEqual(decode(rep), errors.SUCCESS)
        rep = c.get('/user/register', {'username': 'jack2', 'password': self.good_password})
        self.assertEqual(decode(rep), errors.LOGGED_IN)

    def test_register_success(self):
        c = Client()
        rep = c.get('/user/register', {'username': 'hello', 'password': self.good_password})
        self.assertEqual(decode(rep), errors.SUCCESS)

    def test_login_insufficient_arguments(self):
        c = Client()
        rep1 = c.post('/user/login')
        rep2 = c.post('/user/login', {'username': 'hello'})
        rep3 = c.post('/user/login', {'password': 'hello-world'})
        self.assertEqual(rep1.status_code, 200)
        self.assertEqual(rep2.status_code, 200)
        self.assertEqual(rep3.status_code, 200)
        self.assertContains(rep1, "Insufficient arguments")
        self.assertContains(rep2, "Insufficient arguments")
        self.assertContains(rep3, "Insufficient arguments")

    def test_login_invalid_creds(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspwwrong'})
        self.assertEqual(decode(rep), errors.INVALID_CREDS)

    def test_login_user_not_exists(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'doesnotexist', 'password': 'whatever'})
        self.assertEqual(decode(rep), errors.USER_NOT_EXISTS)

    def test_login_logged_in(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspw'})
        self.assertEqual(decode(rep), errors.SUCCESS)
        rep = c.post('/user/login', {'username': 'jack', 'password': 'iamafool'})
        self.assertEqual(decode(rep), errors.LOGGED_IN)

    def test_logout_not_logged_in(self):
        c = Client()
        rep = c.post('/user/logout')
        self.assertEqual(decode(rep), errors.NOT_LOGGED_IN)

    def test_logout_success(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspw'})
        self.assertEqual(decode(rep), errors.SUCCESS)
        rep = c.post('/user/logout')
        self.assertEqual(decode(rep), errors.SUCCESS)

    def test_profile_not_logged_in(self):
        c = Client()
        rep = c.post('/user/profile')
        self.assertEqual(decode(rep)['err_code'], errors.NOT_LOGGED_IN['err_code'])
        self.assertEqual(decode(rep)['err_msg'], errors.NOT_LOGGED_IN['err_msg'])
        self.assertEqual(decode(rep)['username'], '')

    def test_profile_success(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspw'})
        self.assertEqual(decode(rep), errors.SUCCESS)
        rep = c.post('/user/profile')
        self.assertEqual(decode(rep)['err_code'], errors.SUCCESS['err_code'])
        self.assertEqual(decode(rep)['err_msg'], errors.SUCCESS['err_msg'])
        self.assertEqual(decode(rep)['username'], 'john')

    def test_profile_last_ip_login(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspw'})
        self.assertEqual(decode(rep), errors.SUCCESS)
        self.assertEqual(self.john.last_ip, '127.0.0.1')

    def test_profile_last_ip_logout(self):
        c = Client()
        rep = c.post('/user/login', {'username': 'john', 'password': 'thisisjohnspw'})
        self.assertEqual(decode(rep), errors.SUCCESS)
        rep = c.post('/user/logout')
        self.assertEqual(decode(rep), errors.SUCCESS)
        self.assertEqual(self.john.last_ip, '127.0.0.1')

    def test_profile_last_ip_register(self):
        c = Client()
        rep = c.post('/user/register', {'username': 'hello', 'password': self.good_password})
        self.assertEqual(decode(rep), errors.SUCCESS)
        user = User.objects.get(username='hello')
        profile = Profile.objects.get(user_id=user.id)
        self.assertEqual(profile.last_ip, '127.0.0.1')
