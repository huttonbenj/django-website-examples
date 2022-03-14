from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('single/<slug:slug>/', views.single, name='blog_single'),
]

