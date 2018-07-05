from django.urls import path
import user.views

urlpatterns = [
    path('register', user.views.register),
    path('login', user.views.login),
    path('logout', user.views.logout),
]
