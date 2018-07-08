from django.test import TestCase, Client
from .views import login, register, logout, profile
from .models import User
from .forms import RegisterForm, UserForm
class LoginTest(TestCase):
    def test_if_login(self):
        response = self.client.post('/register/',{"username" : "test", "password" : "test"})
        print(response.content)
        response = self.client.post('/register/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.post('/register/',{"username" : "aab", "password" : "aa"})
        print(response.content)
        response = self.client.post('/login/',{"username" : "aa", "password" : "a"})
        print(response.content)
        response = self.client.post('/login/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.post('/login/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.get('/profile/')
        print(response.content)
        response = self.client.get('/logout/')
        print(response.content)
        response = self.client.get('/logout/')
        print(response.content)
        response = self.client.get('/profile/')
        print(response.content)
        response = self.client.post('/login/',{"username" : "aaa", "password" : "aa"})
        print(response.content)
        response = self.client.get('/logout/')
        print(response.content)