from django.urls import path
from . import views

urlpatterns = [
    path('', views.ownership, name='ownership'),
]
