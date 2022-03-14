from django.urls import path
from . import views

urlpatterns = [
    path('', views.beach_access, name='beach_access'),
]

