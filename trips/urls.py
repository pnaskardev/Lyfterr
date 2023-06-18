
from django.urls import path

from .views import TripView

app_name='lyfterr'

urlpatterns=[
    path('',TripView.as_view({'get':'list'}),name='trip-list'),
]