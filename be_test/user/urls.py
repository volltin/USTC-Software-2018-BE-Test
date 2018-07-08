from django.conf.urls import url

from . import views

app_name = 'user'
urlpatterns = [
    url(r'^index/', views.index, name='Index'),
    url(r'^login/', views.login, name='Login'),
    url(r'^register/', views.register, name='Register'),
    url(r'^profile/$', views.profile, name='Profile'),
    url(r'^logout/$', views.logout, name='Logout'),
]