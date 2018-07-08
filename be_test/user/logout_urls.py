from django.urls import path

from . import views

urlpatterns = [
    path('', views.logout, name = 'logout'),
]