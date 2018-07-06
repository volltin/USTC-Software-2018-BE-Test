from django.urls import path
import chart.views

urlpatterns = [
    path('simple', chart.views.simple),
]
