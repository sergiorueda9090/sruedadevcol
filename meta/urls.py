from django.urls import path

from . import views

app_name = 'meta'

urlpatterns = [
    path('track-lead/', views.track_lead, name='track_lead'),
]
