from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('single/<slug:slug>', views.single, name='event_single'),
]

