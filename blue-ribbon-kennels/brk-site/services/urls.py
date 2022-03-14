from django.urls import path
from .views import service

urlpatterns = [
    path('<str:service>/', service, name='service'),
]