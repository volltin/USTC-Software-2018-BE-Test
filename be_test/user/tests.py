from django.test import TestCase, Client
from .views import login
from .models import User

class LoginTest(TestCase):
    def test_if_login(self):
        response = self.client.post('/user/register/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.post('/user/register/',{"username" : "aab", "password" : "aa"})
        print(response.content)
        response = self.client.post('/user/login/',{"username" : "aa", "password" : "a"})
        print(response.content)
        response = self.client.post('/user/login/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.post('/user/login/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.get('/user/profile/')
        print(response.content)
        response = self.client.get('/user/logout/')
        print(response.content)
        response = self.client.get('/user/logout/')
        print(response.content)
        response = self.client.get('/user/profile/')
        print(response.content)
        response = self.client.post('/user/login/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.get('/user/logout/')
        print(response.content)