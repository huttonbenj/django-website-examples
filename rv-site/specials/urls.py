from django.urls import path
from . import views

# trying to fix 
urlpatterns = [
    path('', views.specials_feed, name='specials'),
]
