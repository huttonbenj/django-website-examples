from django.urls import path
from .views import index, ajax_submit

urlpatterns = [
    path('', index, name='contact'),
    path('ajax/submit/', ajax_submit),
]