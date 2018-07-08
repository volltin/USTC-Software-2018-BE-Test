from django.conf.urls import url
from . import views


app_name = 'chart'
urlpatterns = [
    url(r'^index/', views.index, name='Index'),
    url(r'^simple/', views.plot, name='Plot'),
]