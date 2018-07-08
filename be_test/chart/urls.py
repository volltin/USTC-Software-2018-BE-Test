from django.conf.urls import url
from . import views


app_name = 'chart'
urlpatterns = [
    url(r'^/', views.plot, name = 'Plot'),
    url(r'^simple/', views.plot, name='Plot'),
]